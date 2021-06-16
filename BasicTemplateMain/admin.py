from django.contrib.admin import AdminSite

class EmployeeAdminSite(AdminSite):
    site_header = 'Coffeehouse Employee admin'

superadmin = EmployeeAdminSite(name='superadmin')


class ProviderAdminSite(AdminSite):
    site_header = 'Coffeehouse Provider admin'

provideradmin = ProviderAdminSite(name='provideradmin')