#

n = nil
s = nil
a = nil

def opros(n, s, a)
	if a < 18
		puts " Hello, #{n} #{s}, самое время научится"
	else
		puts "Hello #{n} #{s}, еще не поздно начать"
	end
end

Print "your name"
n = gets
Print "your surname"
s = gets
Print "your age"
a = gets.to_i

opros(n,s,a)




