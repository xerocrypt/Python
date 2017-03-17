{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgLoginScreen',
          'title':u'Login Screen',
          'size':(432, 152),
          'foregroundColor':(0, 0, 0),
          'backgroundColor':(187, 187, 187),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'TextField', 
    'name':'txtHash', 
    'position':(22, 36), 
    'size':(389, -1), 
    'alignment':u'center', 
    'backgroundColor':(88, 255, 121, 255), 
    'text':u'HASH VALUE', 
    },

{'type':'Button', 
    'name':'cmdSetPassword', 
    'position':(170, 70), 
    'label':u'Set', 
    },

{'type':'PasswordField', 
    'name':'txtPassword', 
    'position':(22, 4), 
    'size':(391, -1), 
    'backgroundColor':(45, 255, 92, 255), 
    },

{'type':'Button', 
    'name':'cmdCancel', 
    'position':(70, 70), 
    'label':u'Hash', 
    },

{'type':'Button', 
    'name':'cmdLogin', 
    'position':(270, 70), 
    'label':u'Login', 
    },

] # end components
} # end background
] # end backgrounds
} }
