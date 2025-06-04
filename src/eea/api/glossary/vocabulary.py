# -*- coding: utf-8 -*-
""" GlossaryTermsVocabulary """
import json
import os
from elasticsearch import Elasticsearch
from zope.globalrequest import getRequest
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer


HEADERS = {
    "Accept": "application/vnd.elasticsearch+json; compatible-with=8",
    "Content-Type": "application/vnd.elasticsearch+json; compatible-with=8"
}


@implementer(IContextSourceBinder)
class GlossaryTermsVocabulary(object):
    """ GlossaryTermsVocabulary """
    # def __init__(self, term=''):
    # self.term = term

    def __call__(self, context):
        request = getRequest()
        request_title = request.form.get('title', '')
        request_term = ''

        request_token = request.form.get('token', '')
        if request_token:
            request_token_json = json.loads(request_token)
            request_term = request_token_json.get('term', request_title)

        if not request_term:
            request_term = request_title

        terms_vocab = []

        es_dsn = os.environ.get('RAZZLE_PROXY_ES_DSN_globalsearch')
        es_dsn_split = es_dsn.split('/')
        host = "/".join(es_dsn_split[:-1])
        index_name = es_dsn_split[-1]

        # Globalsearch
        es = Elasticsearch(host)
        resp = es.search(
            index=index_name,
            headers=HEADERS,
            query={
                "bool": {
                    "must": [
                        {"match": {"objectProvides": "Glossary term"}},
                        {"query_string": {"default_field": "title",
                                          "query": request_term + '*'}}]}})

        # Wise test temporarily added
        # index_name = 'wisetest_searchui'
        # resp_wise_test = es.search(
        #     index=index_name,
        #     query={
        #         "bool": {
        #             "must": [
        #                 {"match": {"objectProvides": "Glossary term"}},
        #                 {"query_string": {"default_field": "title",
        #                                   "query": request_term + '*'}}]}})

        results = resp["hits"]["hits"]  # + resp_wise_test["hits"]["hits"]

        for item in results:
            term = item['_source']['title']
            sources = []

            if 'term_source' in item['_source']:
                title = item['_source']['term_source']
                link = title if title.startswith('http') else None

                sources.append({
                    'link': link,
                    'organisation': '',
                    'title': item['_source']['term_source']
                })
            else:
                sources = item['_source']['data_provenances']

            if 'term_description' in item['_source']:
                definition = item['_source']['term_description']
            else:
                definition = item['_source']['description']

            term_json = {
                'term': term,
                'definition': definition,
                'sources': sources,
            }
            if definition in ('None', '', None):
                continue

            terms_vocab.append(
                SimpleVocabulary.createTerm(
                    json.dumps(term_json),  # value
                    json.dumps(term_json),  # token
                    json.dumps(term_json),  # title
                )
            )
        return SimpleVocabulary(terms_vocab)


GlossaryTermsVocabularyFactory = GlossaryTermsVocabulary()
