def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars >= 40 and cigars <= 70:
      return True
    else:
      return False
  else:
    if cigars >= 40 and cigars <= 60:
      return True
    else:
      return False
    