grammar = """
  S -> App_Type_Open 'App_Type' AT_to_AS DS| App_Structure_Open AS AS_to_AT DS

  App_Type_Open -> 'A' | 'Create a' | 'Build a' | 'Start with a'
  AT_to_AS -> 'that uses' AS | 'that implements' AS | 'that can perform' AS

  App_Structure_Open -> 'Using' | 'With'
  AS -> 'App_Structure_1' | 'App_Structure_1' 'and' 'App_Structure_2'

  AS_to_AT -> 'implement a' 'App_Type' | 'build a' 'App_Type' | 'construct a' 'App_Type' | 'work on a' 'App_Type' | 'create a' 'App_Type'

  DS -> DS_open 'Data_Set_1' DS_Close | DS_open_2 'Data_Set_1' DS_Close 'and a' 'Data_Set_2' DS_Close

  DS_open -> 'with a' | 'using a'
  DS_open_2 -> 'to combine a' | 'using both a'

  DS_Close -> 'dataset'|'database'

"""