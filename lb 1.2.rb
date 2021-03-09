#

a = nil
b = nil

def sum(a,b)
  if a==20 or b==20
    puts 20
  else
    puts a+b
  end
end

print "a: "
a = gets.to_i
print "b: "
b = gets.to_i

sum(a,b)

puts Thats all
