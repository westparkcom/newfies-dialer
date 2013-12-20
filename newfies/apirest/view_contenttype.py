# -*- coding: utf-8 -*-
#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from rest_framework import viewsets
from apirest.content_type_serializers import ContentTypeSerializer
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class ContentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows content_type to be viewed or edited.
    """
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    authentication = (BasicAuthentication, SessionAuthentication)
    permissions = (IsAuthenticated, DjangoModelPermissions)