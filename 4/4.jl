function parse_range(range)
    x = split(range, "-")
    _x = (parse(Int64, x[1]), parse(Int64, x[2]))
    return _x
end
lines = [[parse_range(line[1]), parse_range(line[2])] for line in map(x -> split(x, ","), readlines("i.txt"))]
lines = [x for x in lines if (x[1][1] in x[2][1]:x[2][2] || x[1][2] in x[2][1]:x[2][2]) || 
        (x[2][1] in x[1][1]:x[1][2] || x[2][2] in x[1][1]:x[1][2])]
print(size(lines))
