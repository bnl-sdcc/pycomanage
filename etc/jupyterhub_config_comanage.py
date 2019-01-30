#
# Example config for cilogon + comanage to control but authN and authZ 
# Creates local account if not arleady presen t
#  eppn -> UNIX   e.g.   jhover@bnl.gov ->jhoverbnlgov
# Local spawner
#
import os
os.environ['CILOGON_HOST'] = 'cilogon.org'
os.environ['CILOGON_CLIENT_ID'] = 'cilogon:/client_id/5ea8818a26318a9dc03d8a1f82bef34a'
os.environ['CILOGON_CLIENT_SECRET'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
os.environ['JUPYTERHUB_CRYPT_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxx'

from oauthenticator.comanage import COManageOAuthenticator, LocalCOManageOAuthenticator
from jupyterhub.comanage import NormalizedSpawner
c.JupyterHub.authenticator_class = LocalCOManageOAuthenticator
c.COManageOAuthenticator.oauth_callback_url = 'https://jupyter05.sdcc.bnl.gov:8000/hub/oauth_callback'
c.COManageOAuthenticator.idp_whitelist = [ 'bnl.gov','anl.gov','ornl.gov', 'lbl.gov']
c.COManageOAuthenticator.comanage_group_whitelist = [ 'CO:members:active','bnl' ]
c.JupyterHub.cookie_secret_file = '/usr/local/anaconda3/etc/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.debug = True
c.JupyterHub.log_level = 10
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'
c.JupyterHub.ssl_cert = '/usr/local/anaconda3/etc/jupyterhub/ssl/certificate.crt'
c.JupyterHub.ssl_key = '/usr/local/anaconda3/etc/jupyterhub/ssl/key.pem'
c.Spawner.debug = True
c.Authenticator.admin_users = {'jhover@bnl.gov'}
c.Authenticator.enable_auth_state = True
c.LocalAuthenticator.create_system_users = True


