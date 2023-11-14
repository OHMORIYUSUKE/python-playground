def SampleCodes(selected_language):
    
    if selected_language == "perl":
        return '''#!/usr/bin/perl

use strict;
use warnings;

my $input = <STDIN>;
chomp($input);

print "hello $input";
'''
    elif selected_language == "go":
        return '''package main

import "fmt"

func main() {
    var input string
    fmt.Scanln(&input)

    fmt.Printf("hello %s", input)
}'''
    elif selected_language == "kotlin":
        return '''fun main() {
    val input = readLine()

    println("hello $input")
}'''
    elif selected_language == "julia":
        return '''input = readline()

println("hello $input")'''
    elif selected_language == "rust":
        return '''use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input = input.trim();

    println!("hello {}", input);
}'''
    elif selected_language == "python":
        return '''
user_input = input()

greeting = f"hello {user_input}"

print(greeting)
'''
    else:
        print("Unsupported language")

