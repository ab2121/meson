project('modules_test', 'c')

case_num = get_option('case_num')

if case_num == 0
  dep_mods = dependency('modules') # all modules
elif case_num == 1
  dep_mods = dependency('modules', modules : ['foo1'])
elif case_num == 2
  dep_mods = dependency('modules', modules : ['foo1', 'foo2'])
elif case_num == 3
  dep_mods = dependency('modules', modules : ['foo3'])
elif case_num == 4
  dep_mods = dependency('modules', modules : ['foo4', 'foo5'])
elif case_num == 5
  dep_mods = dependency('modules', modules : ['foo5'])
elif case_num == 6
  dep_mods = dependency('modules', modules : ['foo1', 'foo3', 'foo5'])
else
  error('not supported case')
endif

executable('mod_test', 'prog.c', dependencies : [dep_mods])
