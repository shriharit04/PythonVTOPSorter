from PyPDF2 import PdfReader, PdfWriter
import time

reader =PdfReader("qwerty.pdf")
writer = PdfWriter()

for i in range(1000):
    writer.append(reader)


t0 = time.time()
with open("out-2000-pages.pdf", "wb") as fp:
    writer.write(fp)
t1 = time.time()

print(f"{t1-t0:.2f}s")

