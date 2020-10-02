from algorithms.stack.longest_abs_path import length_longest_path

st= "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdirectory1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
st2 = "a\n\tb1\n\t\tf1.txt\n\taaaaa\n\t\tf2.txt"
print("path:", st2)

print("answer:", length_longest_path(st2))