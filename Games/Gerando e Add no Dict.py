soma=0


def notas(*n,sit=False):
       r=dict()
       r['Total']=len(n)
       r['Maior']=max(n)
       r['Menor']=min(n)
       r['Media']=sum(n)/len(n)
       if sit:
           if r['Media']>=7.0:
               r["Situacao"]='Boa'
           else:
               r['Situacao']='Ruim'
       return r