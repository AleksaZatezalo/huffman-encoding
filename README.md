# Huffman Encoding
Huffman encoding is a form of lossless compression. Huffman encoding is implemented in python.

# Introduction
Huffman encoding is an algorithm for lossless compression developed David A. Huffman during his Ph.D in computer science at MIT. The algorithm was created when a professor offered his students the option of taking a final exam or the option of improving a leading compression algorithm. The algorithm performs lossless compression by ordering characters  in a file according to there frequency of appearance. They are sorted into a tree and given a variable length byte code with lesser occurring frequencies having longer codes.

## Terminology 
Huffman coding uses specific methods for determining how each symbol is represented. This results in a list of codes called prefix codes, that is to say that any one particular symbol is never the prefix of another. The term "Huffman code" is sometimes used to refer to prefix codes even though the codes may have never been produced by Huffman's algorithms.

## Problem Definition
Given a set of symbols and their frequency of occurrence (proportionate to there frequency of occurrence), we must find a prefix-free binary tree with the minimum expected code-word length. Each code must be uniquely decodeable. The sum of probabilities for the occurrence of each symbol must add to one. 

### Shannon's Source Coding Theorem
Named after Claude Shannon; a mathematician and Scientist, Shannon's source coding theorem (or noiseless coding theorem) sets statistical limits to data compression. The theorem places an upper and lower limit to the expected length of prefix codes as a function of information entropy. 
Information entropy (also refereed to as Shannon entropy), defines data communication systems as composed of three elements: Data source, communication channels, and receivers. The fundamental problem of communication, as per this model, is for the receiver to identify what data was generated by the source. Information entropy is modeled after thermodynamic entropy and describes a random variables tendency to degenerate over time. It is modeled by this formula where the variable i, is a random variable. It's probability function, p, produces a value between 0 and 1.


# Basic Technique
## Compression
Once the frequency of each occurring symbol is calculated, Huffman's encoding algorithm sorts all symbols into a binary tree. A node can either be an internal node or a leaf node. All nodes initially start as leaf nodes which contain the symbol itself and it's frequency of appearance.  An internal node connects to two leaf nodes (which contain symbols). Internal nodes contains a weight and links to it's two child nodes. Internal nodes are created by linking two leaf notes in order of decreasing probability, and it's weighting is the sum of the child nodes probabilities. Internal nodes are linked together via the same process until one node without a parent exists. This is called the root node. To encode a symbol traverse down the tree starting at the root node. Use '0' to represent the left child and '1' to represent the right child. 

## Decompression
Decompression is simply a matter of converting prefix codes to symbols via the same process as above. However the Huffman tree must be constructed beforehand.

## Contribution Guidelines
When contributing to this repository, please first discuss the change you wish to make via issue here on GitHub. Make sure all pull requests are tagged with a specific ticket number found in the repositories issues section.Before making any changes please create your own branch. Follow all three points below before opening a PR:
1. Any changes you want to create must be tagged to an issue opened on this repo. If an issue you've found does not yet exit, please open it.
2. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
3. Make sure all corresponding test cases pass.
4. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.

## Known Issues
A list of known issues and features that are currently being addressed are maintained on the github issues tab. Please look at the list of known issues before raising a new issue.

## Donation Link
If you have benefited from this project and use Monero please consider donanting to the following address:
47RoH3K4j8STLSh8ZQ2vUXZdh7GTK6dBy7uEBopegzkp6kK4fBrznkKjE3doTamn3W7A5DHbWXNdjaz2nbZmSmAk8X19ezQ
