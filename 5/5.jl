using DataStructures

lines = readlines("i.txt")
stacks = Dict()
moves = []
for i in Iterators.reverse(1:length(lines))
    line = lines[i]
    if (occursin("move", line))
        numbers = map(eachmatch(r"\d+", line)) do m
            parse(Int64, m.match)
        end
        push!(moves, numbers)
    elseif (line != "")
        l = [(line[i-2], trunc(Int, i / 4)) for (i,x) in enumerate(line) if (i % 4 == 0 && isletter(line[i-2]))]
        len = length(line)
        if (isletter(line[len - 1])) push!(l, (line[len - 1], trunc(Int, (len+1) / 4))) end
        for x in l
            if (.!haskey(stacks, x[2]))
                s = Stack{Char}()
                push!(s, x[1])
                stacks[x[2]] = s
            else
                push!(stacks[x[2]], x[1])
            end
        end
        
    end
end

for move in reverse(moves)
    num_moves = move[1]
    for num in 1:num_moves
        box = pop!(stacks[move[2]])
        push!(stacks[move[3]], box)
    end
end

for (key, stack) in stacks
    print(first(stack),"-", key, "\n")
end


