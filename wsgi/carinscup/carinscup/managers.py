from django.db import models
from django.conf import settings
from eventor_toolkit import Eventor


class CompetitorsManager(models.Manager):
    def update_from_eventor(self):
        e = Eventor(settings.API_KEY)
        competitors = e.members_in_organisation(settings.ORGANISATION_ID)
        for c in competitors:
            competitor_id = c['PersonId']['#text']
            given_name = c['PersonName']['Given']['#text']
            family_name = c['PersonName']['Family']
            sex = c['@sex']
            birth_date = c['BirthDate']['Date']
            self.update_or_create(
                competitor_id=competitor_id,
                defaults={
                    'given_name': given_name,
                    'family_name': family_name,
                    'sex': sex,
                    'birth_date': birth_date})
