# # from celery import Celery
#
#
# # # todo: make the same celery usable over multiple files
# # app = Flask(__name__)
# # app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# # app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# #
# # celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# # celery.conf.update(app.config)
#
# from celery import Celery
#
# def make_celery(app):
#     celery = Celery(app.import_name)
#     celery.conf.update(app.config["CELERY_CONFIG"])
#
#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)
#
#     celery.Task = ContextTask
#     return celery
#
#

# ### Zombied on Nov 7
