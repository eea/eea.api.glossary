# -*- coding: utf-8 -*-
from zope.globalrequest import getRequest
import json
import os
from elasticsearch import Elasticsearch
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer


@implementer(IContextSourceBinder)
class GlossaryTermsVocabulary(object):
    """ GlossaryTermsVocabulary """
    # def __init__(self, term=''):
    # self.term = term

    def __call__(self, context):
        request = getRequest()
        request_title = request.form.get('title', '')
        print(request_title)
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

        es = Elasticsearch(host)

        resp = es.search(
            index=index_name,
            query={
                "bool": {
                    "must": [
                        {"match": {"objectProvides": "Glossary term"}},
                        {"query_string": {"default_field": "title",
                                          "query": request_term + '*'}}]}})

        for item in resp["hits"]["hits"]:
            # import pdb
            # pdb.set_trace()
            term = item['_source']['title']
            # url = item['_source']['about']
            source = item['_source']['term_source']
            definition = item['_source']['term_description']
            term_json = {
                'term': term,
                'definition': definition,
                'source': source,
            }
            if definition in ('None', '', None):
                continue

            # items.append({"term": term,
            #              "definition": [definition]})

            terms_vocab.append(
                SimpleVocabulary.createTerm(
                    json.dumps(term_json),  # value
                    json.dumps(term_json),  # token
                    json.dumps(term_json),  # title
                )
            )

        # import pdb; pdb.set_trace()
        return SimpleVocabulary(terms_vocab)


GlossaryTermsVocabularyFactory = GlossaryTermsVocabulary()
