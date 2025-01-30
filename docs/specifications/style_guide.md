# Sanskrit Programming Language Style Guide

## Introduction

This style guide provides guidelines for writing clean, maintainable, and idiomatic Sanskrit Programming Language code. Following these conventions will help ensure consistency across projects and make code more readable for all developers.

## 1. File Organization

### 1.1 File Names
- Use `.sam` extension for source files
- Use lowercase Sanskrit words with underscores
- Example: `क्रम_विधि.sam`, `गणित_उपयोग.sam`

### 1.2 File Structure
1. File description comment
2. Module imports
3. Constants
4. Type definitions
5. Function definitions
6. Main program code

## 2. Formatting

### 2.1 Indentation
- Use 4 spaces for indentation
- No tabs
- Align nested blocks consistently

### 2.2 Line Length
- Maximum 80 characters per line
- Break long lines at logical points
- Use line continuation for long expressions

### 2.3 Spacing
- One space after keywords
- No space after function names
- One space around operators
- No space inside parentheses
- One space after commas

## 3. Naming Conventions

### 3.1 Variables
- Use meaningful Sanskrit words
- Follow Sanskrit grammar rules
- Use camelCase for compound words
- Example: `पुस्तकसूची`, `वर्तमानमूल्य`

### 3.2 Functions
- Use verb-based names
- End with appropriate विभक्ति
- Example: `गणयति()`, `परिवर्तयति()`

### 3.3 Classes
- Use noun-based names
- Start with capital letter
- Example: `पुस्तकम्`, `विद्यार्थी`

### 3.4 Constants
- All uppercase
- Separate words with underscores
- Example: `परम_मूल्य`, `न्यून_सीमा`

## 4. Comments and Documentation

### 4.1 File Headers
```sanskrit
// फाइलनाम: calculation.sam
// लेखक: नाम
// दिनाङ्क: YYYY-MM-DD
// विवरण: Brief description in Sanskrit
```

### 4.2 Function Documentation
```sanskrit
// क्रिया: योगः
// कार्यम्: Adds two numbers
// प्रवेशः: 
//   - प्रथमः: First number
//   - द्वितीयः: Second number
// प्रतिफलम्: Sum of the numbers
क्रिया योगः(संख्या प्रथमः, संख्या द्वितीयः) {
    // ...
}
```

### 4.3 Inline Comments
- Use Sanskrit for logical explanations
- Use English for technical clarifications
- Keep comments concise and meaningful

## 5. Code Organization

### 5.1 Function Structure
- Single responsibility principle
- Maximum 20 lines per function
- Clear input/output documentation
- Proper error handling

### 5.2 Class Structure
- Logical grouping of methods
- Clear inheritance hierarchy
- Proper encapsulation
- Documented public interface

## 6. Best Practices

### 6.1 Error Handling
```sanskrit
प्रयत्न {
    // Risky code
} रक्षण (दोषः) {
    // Error handling
}
```

### 6.2 Variable Declaration
```sanskrit
संख्या मूल्यम् = ०;  // Initialize with default
सूची फलानि = [];    // Empty collection
```

### 6.3 Loop Constructs
```sanskrit
कृते (संख्या इ = ०; इ < सीमा; इ = इ + १) {
    // Indexed loop
}

यावत् (शर्त) {
    // Condition-based loop
}
```

## 7. Performance Considerations

### 7.1 Memory Usage
- Proper resource cleanup
- Avoid memory leaks
- Use appropriate data structures

### 7.2 Optimization
- Clear over clever
- Profile before optimizing
- Document performance-critical sections

## 8. Testing

### 8.1 Test File Organization
- Test files end with `_परीक्षा.sam`
- One test file per source file
- Organized by functionality

### 8.2 Test Structure
```sanskrit
परीक्षा वर्गः योगपरीक्षा {
    क्रिया सामान्ययोगः() {
        // Test case
    }
}
```

## 9. Version Control

### 9.1 Commit Messages
- Sanskrit summary line
- Detailed description in Sanskrit/English
- Reference related issues

### 9.2 Branch Names
- feature/description
- fix/description
- docs/description

## 10. Examples

### 10.1 Well-Formatted Code
```sanskrit
// Calculate factorial
क्रिया क्रमगुणनम्(संख्या अङ्कः) {
    यदि (अङ्कः <= १) {
        प्रतिफल १;
    }
    
    प्रतिफल अङ्कः * क्रमगुणनम्(अङ्कः - १);
}
```

### 10.2 Class Definition
```sanskrit
वर्गः पुस्तकम् {
    // Properties
    नाम;
    लेखकः;
    
    // Constructor
    क्रिया जन्म(नामपरम्, लेखकपरम्) {
        अस्य.नाम = नामपरम्;
        अस्य.लेखकः = लेखकपरम्;
    }
}
``` 