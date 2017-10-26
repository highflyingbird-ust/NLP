x = float(input('Enter vocab size: '));
ram = float((x*300*4)/(1024**3));
if ram*100<10:
    ram=ram*1024;
    print("%.2f MB" % ram)
else:
    print("%.2f GB" % ram)
