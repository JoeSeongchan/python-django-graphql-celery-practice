''''''
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda val: '.png' in val or \
               '.jpg' in val,files)))