text = "X-DSPAM-Confidence:    0.8475"
val=text[text.find(':')+1:]
print(float(val))