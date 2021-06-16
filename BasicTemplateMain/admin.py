from django.contrib.admin import AdminSite

class SuperAdminSite(AdminSite):
    site_header = 'Coffeehouse Employee admin'

superadmin = SuperAdminSite(name='superadmin')

