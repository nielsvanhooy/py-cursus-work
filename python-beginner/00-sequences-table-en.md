# Python Data Structures Comparison

Here's a comprehensive comparison of Python's main built-in data structures:

| Feature | Lists | Dictionaries | Sets | Tuples |
|---------|-------|--------------|------|--------|
| **Syntax** | `[1, 2, 3]` | `{'a': 1, 'b': 2}` | `{1, 2, 3}` | `(1, 2, 3)` |
| **Mutability** | Mutable | Mutable | Mutable | Immutable |
| **Ordered** | Yes | Yes (since Python 3.7) | No | Yes |
| **Indexable** | Yes | No (key access) | No | Yes |
| **Allows Duplicates** | Yes | No (unique keys) | No | Yes |
| **Element Types** | Any | Keys: immutable types<br>Values: any | Immutable types | Any |
| **Time Complexity** ||||
| - Access | O(1) | O(1) | N/A | O(1) |
| - Search | O(n) | O(1) | O(1) | O(n) |
| - Insert/Delete | O(n) | O(1) | O(1) | N/A (immutable) |
| **Memory Usage** | Medium | High | Medium-High | Low |
| **Common Use Cases** | • Ordered collections<br>• Sequences<br>• Stacks/Queues | • Key-value mappings<br>• Lookups<br>• JSON-like data | • Unique elements<br>• Membership testing<br>• Mathematical operations | • Immutable sequences<br>• Dictionary keys<br>• Function returns |
| **Special Operations** | Slicing, sorting, appending | Merging, key/value access | Union, intersection, difference | Unpacking, multiple returns |

Would you like me to explain any particular aspect of these data structures in more detail?