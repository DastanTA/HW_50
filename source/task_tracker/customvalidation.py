from django.core.validators import ValidationError


def banned_words(summary):
    banned = ['sex', 'bomb', 'kill', 'porn', 'секс', 'бомба', 'убью', 'порно']
    summary_lst = summary.split()
    for word in summary_lst:
        if word in banned:
            raise ValidationError("Пожалуйста, не используйте запрещенные слова")
