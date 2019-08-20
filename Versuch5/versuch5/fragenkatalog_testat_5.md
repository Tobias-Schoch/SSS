# Fragenkatalog Testat 5

1. Wie beschreibt man mathematisch die Abtastung eines Signals g(t) zum Zeitpunkt t1?

   - g(t) _ δ(t − i) => g(1) _ δ(1 − 1) = 0

2. Wie sieht das Spektrum einer mit Abtastintervall 1 abgetasteten Funktion mit Spektrum
   G(omega) aus?

   - Spektrum des ursprünglichen, nicht abgetasteten Signals wird
     unendlich oft an jedem Puls der Kammfunktion
     repliziert. Das resultierende Spektrum ist also periodisch mit
     Periode ωs = 2π/τ (Abtastfrequenz).

3. Wie verändert sich das Spektrum einer Kammfunktion, wenn man das Abtastintervall
   verdreifacht?

   - FT der Kammfunktion ist wieder eine Kammfunktion wenn man das Abtastintervall verdreifacht folgt daraus => Abtastfrequenz * 1/3, also FT von III( 1/3*x ) => 3*III(3/(2*PI)\*omega) (S22).
     Spektrum wird 3 mal genauer/feiner ( enthaelt 3 mal so viele Abtastpunkte)

4. Unter welchen Bedingungen entsteht Aliasing?

   - Ist die Abtastfrequenz
     kleiner als die doppelte
     Grenzfrequenz des
     Signals, so überlappen
     die Kopien des
     Spektrums.

5. Wie funktioniert das Sägezahnverfahren bei der A/D-Wandlung?

- nach dem Zählverfahren: es wird abgezählt, wie oft man eine dem LSB
  entsprechende Referenzspannung addieren muss, um die
  Eingangsspannung zu erhalten. Die Zahl der Schritte ist gleich
  dem Ergebnis. Es geht dementsprechend langsam, der Aufwand
  dafür ist aber klein

6. Welche scheinbare Frequenz hat ein Sinussignal der Frequenz f0, wobei f0 größer als die
   Nyquistfrequenz, aber kleiner als die Abtastfrequenz f1 ist?

- ?

7. Was ist Aliasing?

- Überlappung

8. Wie schafft man es, die Fouriertransformierte eines diskreten Signals im Computer zu #
   berechnen, obwohl seine Fouriertransformierte kontinuierlich ist?

- Das Eingangssignal wird periodisch fortgesetzt, um so die diskrete Fourierreihe berechnen zu können.
  Dadurch wird das Spektrum diskret und periodisch, aber unendlich.
  Repräsentiert wird das Signal um das Spektrum im Rechner jeweils nur durch eine Periode

9. Ist die diskrete Fouriertransformation und die Fouriertransformation bei zeitdiskreten
   Signalen das Gleiche?

   - Nein. Wiki sagt: Die Diskrete Fourier-Transformation ist von der verwandeten Fouriertransformation für zeitdiskrete Signale zu unterscheiden, welche aus zeitdiskreten Signal ein kontinuierliches Frequenzspektrum bildet.
     Nein. Skript sagt: Die zeitdiskrete Fourierstransformation führt zu kontinuierlichen Spektren

10. Was ist ein FIR-Filter?

- Finite Impulse Response
  Prinzip: durch eine Serie von N Verzögerungsgliedern τ stehen die
  letzten N Eingangswerte zur Verfügung, die mit den
  Filterkoeizienten ck multipliziert und dann aufsummiert werden.
  Die Werte der Filterkoeizienten sind die Impulsantwort, d.h.
  ck = h[k], k = 0, . . . , N.

11. Was ist ein FFT-Filter?

- Prinzip: Signal über FFT in den Frequenzbereich
  transformieren, unerwünschte Frequenzbereiche auf Null setzen
  (Real-und Imaginärteil, dabei Symmetrien beachten!), über IFFT
  wieder in den Zeitbereich zurücktransformieren.
  Beinahe perfekte Filtereigenschaen: die Flankensteilheit liegt
  an der physikalisch durch die Unschärferelation bezeichneten
  Grenze (z.B. Sprung von 0 auf 1 innerhalb einer Bandbreite von 1
  Hz bei einer Signallänge von 1 s). Die Flankensteilheit des Filters
  hängt also lediglich von der Zeitdauer des Signals bzw.
  Datenblocks ab!
  Absolute Phasenlinearität, d.h. die Form bzw. Symmetrie der
  Signale im Zeitbereich wird nicht verändert.
  Nachteile: hoher Rechenaufwand, lang andauernde Signale
  müssen in Blöcke zerlegt werden, Filter kann nicht in Echtzeit
  mitlaufen.

12. Wieviele Fourierkoeffizienten hat die Fourierreihe eines diskreten Signals, das aus 8
    Abtastpunkten besteht?

    - 8

13. Warum braucht man bei diskreten periodischen Signalen nur endliche Fourierreihen zu
    ihrer Darstellung?

    - Für ein diskretes, periodisches Signal mit der Periode N gibt es
      nur N verschiedene periodische Grundsignale
    - Die Fourierreihe dieser Signale besteht daher nur aus N Termen

14. Was sind die Unterschiede zwischen den Analysegleichungen der diskreten und
    kontinuierlichen Fourierreihe?

    - diskret: Summe
    - kontinuierlich: Integral von T bis 0

15. Warum reicht bei diskreten linearen Systemen die Antwort auf einen Einheitsimpuls zum
    Zeitpunkt 0, um es vollständig zu charakterisieren?

    - Jedes diskrete Signal lässt sich als gewichtete Summe von Einheitsimpulsen darstellen

    - Ist der Output eines linearen Systems für jeden um k verschobenen Einheitsimpuls bekannt, so kann die Systemantwort auf jedes beliebige Inputsignal ausgedrückt werden

16. Wie berechnet man die Systemantwort eines diskreten linearen Systems?

    - Auch in diesem Fall reicht die Angabe der Impulsantwort h[n] = h0[n], um die Systemantwort für jeden beliebigen Input zu charakterisieren.

17. Was ist der Hauptunterschied zwischen dem Spektrum eines aperiodischen
    kontinuierlichen Signals und dem eines aperiodischen diskreten Signals?

    - aperiodisch kont. => Spektrum: kont., aperiodisches Spektrum
      aperiodisch diskret => Spektrum: kont., periodisches Spektrum

18. Wie sieht ein idealer zeitdiskreter Tiefpass im Spektralraum aus?

    - Nichtkausal
      Unendlich große
      Impulsantwort
      (Sinc-Funktion)
      Überschwingen
      Oszillierendes Einschwingen.

19. Ein zeitdiskreter Filter besteht aus der Differenz des momentanen Inputwertes und des
    Inputwertes des vergangenen Zeitschritts. Um was für eine Art von Filter handelt es sich?
    - ?
20. Ist eine zeitdiskrete Sinusschwingung immer periodisch?
    - Abgetastete Sinusschwingungen sind i.A. nicht periodisch!
      Periodizität gibt es nur, wenn die Periode ein ganzzahliges
      Vielfaches der Abtastzeit ist.
