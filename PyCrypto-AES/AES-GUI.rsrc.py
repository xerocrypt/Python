{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgAESGUI',
          'title':u'AES Message Encryption',
          'size':(475, 267),

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

{'type':'Button', 
    'name':'cmdDecrypt', 
    'position':(370, 75), 
    'label':u'Decrypt', 
    },

{'type':'Button', 
    'name':'cmdEncrypt', 
    'position':(370, 35), 
    'label':u'Encrypt', 
    },

{'type':'StaticText', 
    'name':'lblTitle', 
    'position':(10, 6), 
    'backgroundColor':(84, 84, 84, 255), 
    'font':{'style': 'bold', 'faceName': u'Arial', 'size': 14}, 
    'foregroundColor':(57, 255, 82, 255), 
    'text':u'AES Message Encryption', 
    },

{'type':'PasswordField', 
    'name':'txtPass', 
    'position':(10, 34), 
    'size':(337, -1), 
    'backgroundColor':(27, 255, 71, 255), 
    },

{'type':'TextArea', 
    'name':'txtMessage', 
    'position':(10, 67), 
    'size':(337, 162), 
    'backgroundColor':(27, 255, 71, 255), 
    'text':u':>', 
    },

] # end components
} # end background
] # end backgrounds
} }
