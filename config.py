#------------------------------------------------------------------------------
# NotebookApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## 设置Access-Control-Allow-Credentials:true报头
#c.NotebookApp.allow_credentials = False

## Set the Access-Control-Allow-Origin header
#  
#  Use '*' to allow any origin to access your server.
#  
#  Takes precedence over allow_origin_pat.
#c.NotebookApp.allow_origin = ''

## Use a regular expression for the Access-Control-Allow-Origin header
#  
#  Requests from an origin matching the expression will get replies with:
#  
#      Access-Control-Allow-Origin: origin
#  
#  where `origin` is the origin of the request.
#  
#  Ignored if allow_origin is set.
#c.NotebookApp.allow_origin_pat = ''

## Allow password to be changed at login for the notebook server.
#  
#  While loggin in with a token, the notebook server UI will give the opportunity
#  to the user to enter a new password at the same time that will replace the
#  token login mechanism.
#  
#  This can be set to false to prevent changing password from the UI/API.
#c.NotebookApp.allow_password_change = True

## Allow requests where the Host header doesn't point to a local server
#  
#  By default, requests get a 403 forbidden response if the 'Host' header shows
#  that the browser thinks it's on a non-local domain. Setting this option to
#  True disables this check.
#  
#  This protects against 'DNS rebinding' attacks, where a remote web server
#  serves you a page and then changes its DNS to send later requests to a local
#  IP, bypassing same-origin checks.
#  
#  Local IP addresses (such as 127.0.0.1 and ::1) are allowed as local, along
#  with hostnames configured in local_hostnames.
#c.NotebookApp.allow_remote_access = False

## 是否允许notebook在root用户下运行.
#c.NotebookApp.allow_root = False

## " Require authentication to access prometheus metrics.
#c.NotebookApp.authenticate_prometheus = True

## Reload the webapp when changes are made to any Python src files.
#c.NotebookApp.autoreload = False

## DEPRECATED use base_url
#c.NotebookApp.base_project_url = '/'

## The base URL for the notebook server.
#  
#  Leading and trailing slashes can be omitted, and will automatically be added.
#c.NotebookApp.base_url = '/'

## Specify what command to use to invoke a web browser when opening the notebook.
#  If not specified, the default browser will be determined by the `webbrowser`
#  standard library module, which allows setting of the BROWSER environment
#  variable to override it.
#c.NotebookApp.browser = ''

## SSL/TLS 认证文件所在全路径.
#c.NotebookApp.certfile = ''

## 用于ssl/tls客户端身份验证的证书颁发证书的完整路径.
#c.NotebookApp.client_ca = ''

## The config manager class to use
#c.NotebookApp.config_manager_class = 'notebook.services.config.manager.ConfigManager'

## The notebook manager class to use.
#c.NotebookApp.contents_manager_class = 'notebook.services.contents.largefilemanager.LargeFileManager'

## Extra keyword arguments to pass to `set_secure_cookie`. See tornado's
#  set_secure_cookie docs for details.
#c.NotebookApp.cookie_options = {}

## The random bytes used to secure cookies. By default this is a new random
#  number every time you start the Notebook. Set it to a value in a config file
#  to enable logins to persist across server sessions.
#  
#  Note: Cookie secrets should be kept private, do not share config files with
#  cookie_secret stored in plaintext (you can read the value from a file).
#c.NotebookApp.cookie_secret = b''

## 存放cookie密钥的文件被保存了.
#c.NotebookApp.cookie_secret_file = ''

## Override URL shown to users.
#  
#  Replace actual URL, including protocol, address, port and base URL, with the
#  given value when displaying URL to the users. Do not change the actual
#  connection URL. If authentication token is enabled, the token is added to the
#  custom URL automatically.
#  
#  This option is intended to be used when the URL to display to the user cannot
#  be determined reliably by the Jupyter notebook server (proxified or
#  containerized setups for example).
#c.NotebookApp.custom_display_url = ''

## 从 `/` 重定向到的默认URL
#c.NotebookApp.default_url = '/tree'

## Disable cross-site-request-forgery protection
#  
#  Jupyter notebook 4.3.1 introduces protection from cross-site request
#  forgeries, requiring API requests to either:
#  
#  - originate from pages served by this server (validated with XSRF cookie and
#  token), or - authenticate with a token
#  
#  Some anonymous compute resources still desire the ability to run code,
#  completely without authentication. These services can disable all
#  authentication and security checks, with the full knowledge of what that
#  implies.
#c.NotebookApp.disable_check_xsrf = False

## Whether to enable MathJax for typesetting math/TeX
#  
#  MathJax is the javascript library Jupyter uses to render math/LaTeX. It is
#  very large, so you may want to disable it if you have a slow internet
#  connection, or for offline use of the notebook.
#  
#  When disabled, equations etc. will appear as their untransformed TeX source.
#c.NotebookApp.enable_mathjax = True

## extra paths to look for Javascript notebook extensions
#c.NotebookApp.extra_nbextensions_path = []

## handlers that should be loaded at higher priority than the default services
#c.NotebookApp.extra_services = []

## Extra paths to search for serving static files.
#  
#  This allows adding javascript/css to be available from the notebook server
#  machine, or overriding individual files in the IPython
#c.NotebookApp.extra_static_paths = []

## Extra paths to search for serving jinja templates.
#  
#  Can be used to override templates from notebook.templates.
#c.NotebookApp.extra_template_paths = []

## 
#c.NotebookApp.file_to_run = ''

## Extra keyword arguments to pass to `get_secure_cookie`. See tornado's
#  get_secure_cookie docs for details.
#c.NotebookApp.get_secure_cookie_kwargs = {}

## Deprecated: Use minified JS file or not, mainly use during dev to avoid JS
#  recompilation
#c.NotebookApp.ignore_minified_js = False

## (bytes/sec) Maximum rate at which stream output can be sent on iopub before
#  they are limited.
#c.NotebookApp.iopub_data_rate_limit = 1000000

## (msgs/sec) Maximum rate at which messages can be sent on iopub before they are
#  limited.
#c.NotebookApp.iopub_msg_rate_limit = 1000

## notebook服务会监听的IP地址.
c.NotebookApp.ip = '*'

## Supply extra arguments that will be passed to Jinja environment.
#c.NotebookApp.jinja_environment_options = {}

## Extra variables to supply to jinja templates when rendering.
#c.NotebookApp.jinja_template_vars = {}

## The kernel manager class to use.
#c.NotebookApp.kernel_manager_class = 'notebook.services.kernels.kernelmanager.MappingKernelManager'

## The kernel spec manager class to use. Should be a subclass of
#  `jupyter_client.kernelspec.KernelSpecManager`.
#  
#  The Api of KernelSpecManager is provisional and might change without warning
#  between this version of Jupyter and the next stable one.
#c.NotebookApp.kernel_spec_manager_class = 'jupyter_client.kernelspec.KernelSpecManager'

## SSL/TLS 私钥文件所在全路径.
#c.NotebookApp.keyfile = ''

## Hostnames to allow as local when allow_remote_access is False.
#  
#  Local IP addresses (such as 127.0.0.1 and ::1) are automatically accepted as
#  local as well.
#c.NotebookApp.local_hostnames = ['localhost']

## Set to True to enable JSON formatted logs. Run "pip install notebook[json-
#  logging]" to install the required dependent packages. Can also be set using
#  the environment variable JUPYTER_ENABLE_JSON_LOGGING=true.
#c.NotebookApp.log_json = False

## The login handler class to use.
#c.NotebookApp.login_handler_class = 'notebook.auth.login.LoginHandler'

## The logout handler class to use.
#c.NotebookApp.logout_handler_class = 'notebook.auth.logout.LogoutHandler'

## The MathJax.js configuration file that is to be used.
#c.NotebookApp.mathjax_config = 'TeX-AMS-MML_HTMLorMML-full,Safe'

## A custom url for MathJax.js. Should be in the form of a case-sensitive url to
#  MathJax, for example:  /static/components/MathJax/MathJax.js
#c.NotebookApp.mathjax_url = ''

## Sets the maximum allowed size of the client request body, specified in the
#  Content-Length request header field. If the size in a request exceeds the
#  configured value, a malformed HTTP message is returned to the client.
#  
#  Note: max_body_size is applied even in streaming mode.
#c.NotebookApp.max_body_size = 536870912

## Gets or sets the maximum amount of memory, in bytes, that is allocated for use
#  by the buffer manager.
#c.NotebookApp.max_buffer_size = 536870912

## Gets or sets a lower bound on the open file handles process resource limit.
#  This may need to be increased if you run into an OSError: [Errno 24] Too many
#  open files. This is not applicable when running on Windows.
#c.NotebookApp.min_open_files_limit = 0

## 将Python模块作为笔记本服务器扩展加载。可以使用条目值来启用和禁用扩展的加载。这些扩展将以字母顺序加载。
#c.NotebookApp.nbserver_extensions = {}

## 用于笔记本和内核的目录。
#c.NotebookApp.notebook_dir = ''

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
c.NotebookApp.open_browser = False

## Hashed password to use for web authentication.
#  
#  To generate, type in a python/IPython shell:
#  
#    from notebook.auth import passwd; passwd()
#  
#  The string should be of the form type:salt:hashed-password.
#c.NotebookApp.password = ''

## Forces users to use a password for the Notebook server. This is useful in a
#  multi user environment, for instance when everybody in the LAN can access each
#  other's machine through ssh.
#  
#  In such a case, serving the notebook server on localhost is not secure since
#  any user can connect to the notebook server via ssh.
#c.NotebookApp.password_required = False

## The port the notebook server will listen on (env: JUPYTER_PORT).
c.NotebookApp.port = 1999

## The number of additional ports to try if the specified port is not available
#  (env: JUPYTER_PORT_RETRIES).
#c.NotebookApp.port_retries = 50

## DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
#c.NotebookApp.pylab = 'disabled'

## If True, display a button in the dashboard to quit (shutdown the notebook
#  server).
#c.NotebookApp.quit_button = True

## (sec) Time window used to check the message and data rate limits.
#c.NotebookApp.rate_limit_window = 3

## 重新运行的异常会遇到加载服务器扩展吗?
#c.NotebookApp.reraise_server_extension_failures = False

## 不赞成使用nbserverextensions
#c.NotebookApp.server_extensions = []

## The session manager class to use.
#c.NotebookApp.session_manager_class = 'notebook.services.sessions.sessionmanager.SessionManager'

## Shut down the server after N seconds with no kernels or terminals running and
#  no activity. This can be used together with culling idle kernels
#  (MappingKernelManager.cull_idle_timeout) to shutdown the notebook server when
#  it's not in use. This is not precisely timed: it may shut down up to a minute
#  later. 0 (the default) disables this automatic shutdown.
#c.NotebookApp.shutdown_no_activity_timeout = 0

## The UNIX socket the notebook server will listen on.
#c.NotebookApp.sock = ''

## The permissions mode for UNIX socket creation (default: 0600).
#c.NotebookApp.sock_mode = '0600'

## Supply SSL options for the tornado HTTPServer. See the tornado docs for
#  details.
#c.NotebookApp.ssl_options = {}

## Supply overrides for terminado. Currently only supports "shell_command". On
#  Unix, if "shell_command" is not provided, a non-login shell is launched by
#  default when the notebook server is connected to a terminal, a login shell
#  otherwise.
#c.NotebookApp.terminado_settings = {}

## Set to False to disable terminals.
#  
#  This does *not* make the notebook server more secure by itself. Anything the
#  user can in a terminal, they can also do in a notebook.
#  
#  Terminals may also be automatically disabled if the terminado package is not
#  available.
c.NotebookApp.terminals_enabled = False

## Token used for authenticating first-time connections to the server.
#  
#  The token can be read from the file referenced by JUPYTER_TOKEN_FILE or set
#  directly with the JUPYTER_TOKEN environment variable.
#  
#  When no password is enabled, the default is to generate a new, random token.
#  
#  Setting to an empty string disables authentication altogether, which is NOT
#  RECOMMENDED.
#c.NotebookApp.token = '<generated>'

## Supply overrides for the tornado.web.Application that the Jupyter notebook
#  uses.
#c.NotebookApp.tornado_settings = {}

## Whether to trust or not X-Scheme/X-Forwarded-Proto and X-Real-Ip/X-Forwarded-
#  For headerssent by the upstream reverse proxy. Necessary if the proxy handles
#  SSL
#c.NotebookApp.trust_xheaders = False

## Disable launching browser by redirect file
#  
#  For versions of notebook > 5.7.2, a security feature measure was added that
#  prevented the authentication token used to launch the browser from being
#  visible. This feature makes it difficult for other users on a multi-user
#  system from running code in your Jupyter session as you.
#  
#  However, some environments (like Windows Subsystem for Linux (WSL) and
#  Chromebooks), launching a browser using a redirect file can lead the browser
#  failing to load. This is because of the difference in file structures/paths
#  between the runtime and the browser.
#  
#  Disabling this setting to False will disable this behavior, allowing the
#  browser to launch by using a URL and visible token (as before).
#c.NotebookApp.use_redirect_file = True

## DEPRECATED, use tornado_settings
#c.NotebookApp.webapp_settings = {}

## Specify Where to open the notebook on startup. This is the `new` argument
#  passed to the standard library method `webbrowser.open`. The behaviour is not
#  guaranteed, but depends on browser support. Valid values are:
#  
#   - 2 opens a new tab,
#   - 1 opens a new window,
#   - 0 opens in an existing window.
#  
#  See the `webbrowser.open` documentation for details.
#c.NotebookApp.webbrowser_open_new = 2

## Set the tornado compression options for websocket connections.
#  
#  This value will be returned from
#  :meth:`WebSocketHandler.get_compression_options`. None (default) will disable
#  compression. A dict (even an empty one) will enable compression.
#  
#  See the tornado docs for WebSocketHandler.get_compression_options for details.
#c.NotebookApp.websocket_compression_options = None

## The base URL for websockets, if it differs from the HTTP server (hint: it
#  almost certainly doesn't).
#  
#  Should be in the form of an HTTP origin: ws[s]://hostname[:port]
#c.NotebookApp.websocket_url = ''
