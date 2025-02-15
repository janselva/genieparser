expected_output = {
   'vrf':{
      'vrf102':{
         'address_family':{
            'ipv6':{
               'prefix':{
                  '::/0':{
                     'output_chain':{
                     },
                     'epoch':0,
                     'sharing':'per-destination',
                     'rib':'[S]',
                     'refcnt':5,
                     'flags':[
                        'sc',
                        'defrt'
                     ],
                     'sources':[
                        'RIB,',
                        'IPL,',
                        'DRH'
                     ],
                     'feature_space':{
                        'iprm':'0x00048000',
                        'broker':{
                           'distribution_priority':1
                        }
                     },
                     'ifnums':{
                        'Loopback102':{
                           'ifnum':55
                        }
                     },
                     'path_list':{
                        '7F7AF54316B8':{
                           'locks':3,
                           'sharing':'per-destination',
                           'flags':'0x69 [shble, rif, rcrsv, hwcn]',
                           'path':{
                              '7F7AF54EDF08':{
                                 'share':'1/1',
                                 'type':'recursive',
                                 'for':'IPv6'
                              }
                           }
                        },
                        '7F7AF5431548':{
                           'locks':2,
                           'sharing':'per-destination',
                           'flags':'0x69 [shble, rif, rcrsv, hwcn]',
                           'path':{
                              '7F7AF54EDD68':{
                                 'share':'1/1',
                                 'type':'recursive',
                                 'for':'IPv6',
                                 'flags':'[dsnt-src-via,'
                              }
                           }
                        },
                        '7F7AF30D7D00':{
                           'locks':3,
                           'sharing':'per-destination',
                           'flags':'0x49 [shble, rif, hwcn]',
                           'path':{
                              '7F7AF54EF4F8':{
                                 'share':'1/1',
                                 'type':'connected prefix',
                                 'for':'IPv6'
                              }
                           }
                        }
                     }
                  }
               }
            }
         }
      }
   }
}