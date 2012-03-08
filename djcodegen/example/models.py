from django.db import models

QUIZ = (
    {'name': 'Favorites',
     'questions': ['food', 'movie', 'color']},
    {'name': 'Knowledge',
     'questions': ['languages', 'degrees', 'certificates']}
)


def generate_model(info):
    name = info['name']
    questions = info['questions']

    def get_absolute_url(self):
        return '/{}/{}/'.format(name.lower(), self.id)

    def __unicode__(self):
        return u', '.join([getattr(self, q) for q in questions])

    fields = {'__module__': __name__,
              'get_absolute_url': get_absolute_url,
              '__unicode__': __unicode__}
    for question in questions:
        fields[question] = models.CharField(max_length=80)
    return type(name, (models.Model,), fields)


for topic in QUIZ:
    locals()[topic['name']] = generate_model(topic)