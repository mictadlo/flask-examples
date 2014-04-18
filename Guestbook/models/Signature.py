# -*- coding: utf-8 -*-
import datetime
from flaskext.couchdb import (CouchDBManager, Document, TextField,
                              DateTimeField, ViewField, paginate)



# model
class Signature(Document):
    doc_type = 'signature'

    message = TextField()
    author = TextField()
    time = DateTimeField(default=datetime.datetime.now)

    all = ViewField('guestbook', '''
       function (doc) {
           if (doc.doc_type == 'signature') {
               emit(doc.time, doc);
           };
       }''', descending=True)


manager = CouchDBManager()
manager.add_document(Signature)