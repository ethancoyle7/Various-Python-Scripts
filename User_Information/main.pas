program People;

type
  TPerson = record
    firstName : string;
    lastName : string;
    age : integer;
    occupation : string;
    streetNumber : string;
    address : string;
  end;

var
  people : array of TPerson;
  numPeople : integer;
  i : integer;
  firstName : string;
  lastName : string;
  ageStr : string;
  age : integer;
  occupation : string;
  streetNumber : string;
  address : string;

begin
  write('How many people would you like to add? ');
  readln(numPeople);
  setlength(people, numPeople);
  for i := 0 to numPeople - 1 do
  begin
    repeat
      write('What is the person''s first name? ');
      readln(firstName);
    until (pos('0'..'9', firstName) = 0);
    repeat
      write('What is the person''s last name? ');
      readln(lastName);
    until (pos('0'..'9', lastName) = 0);
    repeat
      write('What is the person''s age? ');
      readln(ageStr);
      repeat
      write('What is the person''s occupation? ');
      readln(occupation);
    until (pos('0'..'9', occupation) = 0);
    repeat
      write('What is the person''s street number? ');
      readln(streetNumber);
    until (pos('0'..'9', streetNumber) <> 0);
    repeat
      write('What is the person''s address? ');
      readln(address);
    until (pos('0'..'9', address) = 0);
    people[i].firstName := firstName;
    people[i].lastName := lastName;
    people[i].age := age;
    people[i].occupation := occupation;
    people[i].streetNumber := streetNumber;
    people[i].address := address;
  end;
  for i := 0 to numPeople - 1 do
    writeln(people[i]);
end.
