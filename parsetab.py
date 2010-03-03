
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x03\xd8\xc9Q1\x0e\x13W\xf5\xf7\xacu\x8b$z\xd4'
    
_lr_action_items = {'AND':([2,8,16,17,20,21,22,23,],[-2,18,18,-5,-7,-6,-3,18,]),'WORD':([0,1,3,5,6,7,9,10,11,12,13,14,15,18,19,],[-16,-16,-9,-8,-16,-16,-10,20,-13,-11,-14,-12,-15,-16,-16,]),'AUTHOR':([0,1,3,5,6,7,9,18,19,],[-16,11,-9,-8,-16,-16,-10,-16,-16,]),'TITLE':([0,1,3,5,6,7,9,18,19,],[-16,12,-9,-8,-16,-16,-10,-16,-16,]),'OR':([2,8,16,17,20,21,22,23,],[-2,19,19,-5,-7,-6,-3,-4,]),'CONTENT':([0,1,3,5,6,7,9,18,19,],[-16,13,-9,-8,-16,-16,-10,-16,-16,]),'LINK':([0,1,3,5,6,7,9,18,19,],[-16,14,-9,-8,-16,-16,-10,-16,-16,]),'LPAREN':([0,6,7,18,19,],[6,6,6,6,6,]),'NOT':([0,6,7,18,19,],[7,7,7,7,7,]),'PLUS':([0,6,7,18,19,],[5,5,5,5,5,]),'$end':([2,4,8,17,20,21,22,23,],[-2,0,-1,-5,-7,-6,-3,-4,]),'MINUS':([0,6,7,18,19,],[3,3,3,3,3,]),'RPAREN':([2,16,17,20,21,22,23,],[-2,21,-5,-7,-6,-3,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'qualifier':([1,],[10,]),'type':([0,6,7,18,19,],[1,1,1,1,1,]),'rule':([0,6,7,18,19,],[2,2,2,2,2,]),'filter':([0,],[4,]),'expression':([0,6,7,18,19,],[8,16,17,22,23,]),'empty':([0,1,6,7,18,19,],[9,15,9,9,9,9,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> filter","S'",1,None,None,None),
  ('filter -> expression','filter',1,'p_filter','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',161),
  ('expression -> rule','expression',1,'p_expression_rule','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',165),
  ('expression -> expression AND expression','expression',3,'p_expression_and','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',169),
  ('expression -> expression OR expression','expression',3,'p_expression_or','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',173),
  ('expression -> NOT expression','expression',2,'p_expression_not','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',177),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',181),
  ('rule -> type qualifier WORD','rule',3,'p_rule','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',185),
  ('type -> PLUS','type',1,'p_type','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',189),
  ('type -> MINUS','type',1,'p_type','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',190),
  ('type -> empty','type',1,'p_type','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',191),
  ('qualifier -> TITLE','qualifier',1,'p_qualifier','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',195),
  ('qualifier -> LINK','qualifier',1,'p_qualifier','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',196),
  ('qualifier -> AUTHOR','qualifier',1,'p_qualifier','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',197),
  ('qualifier -> CONTENT','qualifier',1,'p_qualifier','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',198),
  ('qualifier -> empty','qualifier',1,'p_qualifier','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',199),
  ('empty -> <empty>','empty',0,'p_empty','C:\\Documents and Settings\\Michael Fogleman\\My Documents\\Workspace\\Feed Notifier 2\\filters.py',203),
]
