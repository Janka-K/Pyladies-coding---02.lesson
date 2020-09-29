'''Napiš program, který spočítá povrch a objem krychle o straně 2852 cm.
Abys nemusela tolik hledat v učebnici (vlastně Wikipedii): povrch S = 6a2
, objem V = a3

Řešení, pro kontrolu: S = 48803424cm2, V = 23197894208cm3'''

'''a = 2852
povrch = 6 * a ** 2
objem = a ** 3
print("Povrch krychle je",povrch,"cm2")
print("Objem krychle je",objem,"cm3")'''

strana = int(input("Vloz stranu krychle jako cele cislo: "))
povrch = 6 * strana ** 2
objem = strana ** 3
print("Povrch krychle je",povrch,"cm2")
print("Objem krychle je",objem,"cm3")