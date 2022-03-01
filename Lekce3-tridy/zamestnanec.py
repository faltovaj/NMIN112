#!/usr/bin/env python3
# Trida zamestnancu

class Zamestnanec:
    """ Trida k evidenci zamestnancu """
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def __str__(self):
        """ Toto vypise print """
        return f'{self.cele_jmeno()}'   
    
    def __repr__(self):
        """ Toto se dozvime, pokud se zeptame na reprezentaci """
        return f'Zamestnanec({self.jmeno}, {self.prijmeni})'

    def __eq__(self, other):
        """ Definice pro operator == """ 
        return self.cele_jmeno() == other.cele_jmeno()
    
    def vrat_email(self):
        """ Funkce vrati pracovni email zamestnance """
        return self.jmeno + '.' + self.prijmeni + '@mff.cuni.cz'
    
    def cele_jmeno(self):
        """ Metoda vrati cele jmeno zamestnance """
        return self.jmeno + ' ' + self.prijmeni
    
class Ipnp(Zamestnanec):
    """ Trida Ipnp pro zamestnance na IPNP, dedi z tridy Zamestnanec """
    budova = 'Troja'
    patro = [8, 9]
    _prefix = 'ipnp'            # interni promenna
    def __init__(self, jmeno, prijmeni, kancelar, experiment):
       Zamestnanec.__init__(self, jmeno, prijmeni, kancelar)
       self.experiment = experiment
    def vrat_email(self):
        """ Metoda vrati pracovni email zamestnance na IPNP """
        email = self.prijmeni + '@ipnp.mff.cuni.cz'   
        return email
    def kde_kancelar(self):
        """ Metoda vrati misto, kde najdeme kancelar """
        if self.kancelar[0] == 'A':
             return f'{Ipnp.budova}, patro: {Ipnp.patro[0]}'
        else:
             return f'{Ipnp.budova}, patro: {Ipnp.patro[1]}'
