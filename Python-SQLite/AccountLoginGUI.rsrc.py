{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgAccountLogin',
          'title':u'Account Login',
          'size':(327, 147),
          'statusBar':1,
          'foregroundColor':(94, 255, 97),
          'backgroundColor':(84, 84, 84),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuHelp',
             'label':'&Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpAbout',
                   'label':'&About ...',
                   'command':'doHelpAbout',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'PasswordField', 
    'name':'txtAuthKey', 
    'position':(10, 45), 
    'size':(185, -1), 
    'backgroundColor':(125, 255, 134, 255), 
    },

{'type':'TextField', 
    'name':'txtCurrentUser', 
    'position':(10, 10), 
    'size':(184, -1), 
    'backgroundColor':(92, 247, 103, 255), 
    'text':u'LOGIN', 
    },

{'type':'Button', 
    'name':'cmdLogin', 
    'position':(210, 10), 
    'size':(107, -1), 
    'label':u'Login', 
    },

{'type':'Button', 
    'name':'cmdNewAccount', 
    'position':(210, 50), 
    'label':u'Create Account', 
    },

] # end components
} # end background
] # end backgrounds
} }
