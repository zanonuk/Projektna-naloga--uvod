def izracunaj(izraz):  
    izraz=izraz.replace(':','/')
    pravilen = izraz.find("sin")+izraz.find("cos")+izraz.find("tan")
    if pravilen == -3:
        pravi_izraz=izraz
        return(izraz)
    else:
        st_sin=izraz.count("sin")
        st_cos=izraz.count("cos")
        st_tan=izraz.count("tan")
        indeksi=[]
        index = 0
        if st_sin>0:
            st_sin=0
            while index < len(izraz):
                index = izraz.find('sin', index)
                if index == -1:
                    break
                indeksi.append(index)
                index+=1
            postopek=0
            for i in indeksi:
                if i != indeksi[0]:
                    postopek+=1
                    pom=indeksi[postopek]+(postopek*2)
                    indeksi[postopek]=pom
            for a in indeksi:
                lok=izraz[a:].index("sin")+3
                izraz = izraz[:lok+a]+'('+izraz[lok+a:]
                stevci=['1','2','3','4','5','6','7','8','9','0']
                pom=izraz[lok+a+1:]
                for i in pom:
                    if i in stevci:      
                        lok=lok+1
                    else:
                        break
                izraz = izraz[:lok+a+1]+'*pi/180)'+izraz[lok+a+1:]
        indeksi=[]
        index = 0
        if st_cos>0:
            st_cos=0
            while index < len(izraz):
                index = izraz.find('cos', index)
                if index == -1:
                    break
                indeksi.append(index)
                index+=1
            postopek=0
            for i in indeksi:
                if i != indeksi[0]:
                    postopek+=1
                    pom=indeksi[postopek]+(postopek*2)
                    indeksi[postopek]=pom
            for a in indeksi:
                lok=izraz[a:].index("cos")+3
                izraz = izraz[:lok+a]+'('+izraz[lok+a:]
                stevci=['1','2','3','4','5','6','7','8','9','0']
                pom=izraz[lok+a+1:]
                for i in pom:
                    if i in stevci:      
                        lok=lok+1
                    else:
                        break
                izraz = izraz[:lok+a+1]+'*pi/180)'+izraz[lok+a+1:]
        indeksi=[]
        index = 0
        if st_tan>0:
            st_tan=0
            while index < len(izraz):
                index = izraz.find('tan', index)
                if index == -1:
                    break
                indeksi.append(index)
                index+=1
            postopek=0
            for i in indeksi:
                if i != indeksi[0]:
                    postopek+=1
                    pom=indeksi[postopek]+(postopek*2)
                    indeksi[postopek]=pom
            for a in indeksi:
                #print (a)
                #print (izraz[a:])
                lok=izraz[a:].index("tan")+3
                izraz = izraz[:lok+a]+'('+izraz[lok+a:]
                stevci=['1','2','3','4','5','6','7','8','9','0']
                pom=izraz[lok+a+1:]
                for i in pom:
                    if i in stevci:      
                        lok=lok+1
                    else:
                        break
                izraz = izraz[:lok+a+1]+'*pi/180)'+izraz[lok+a+1:]
        return izraz
