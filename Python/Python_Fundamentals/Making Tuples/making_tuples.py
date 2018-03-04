def convert(d):
    print d.items()
    print [(v, k) for k, v in d.iteritems()]



d = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
convert(d)