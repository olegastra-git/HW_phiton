eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'���������',
      	2:'������',
      	3:'�è��',
      	4:'��',
      	5:'�����',
      	8:'���',
      	10:'���'}
N = abs(int(input('������� 1, ���� ������ � ���������� ���������, ���� 0, ���� � �������: ')))
word = input('������� �����: ').upper()
if N == 1:
	print('�� ���������', sum([k for i in word for k, v in eng.items() if i in v]), '�����')
elif N == 0:
	print('�� ���������', sum([k for i in word for k, v in rus.items() if i in v]), '�����')
else:
    print('������� �� �� ��������!')