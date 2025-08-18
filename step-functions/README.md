# State Functions Guide:
This guide provides an overview of how to use AWS Step Functions to create and manage state machines for various workflows. It includes examples and best practices for defining state machines, integrating with other AWS services, and handling errors.

## Flow for lambda input and output:
1. **State Input**: The input to the state machine can be a JSON object that contains the necessary parameters for the workflow. and which comes from the previous state output or is provided as an input when starting the execution.  
2. **State Input Path**: You can specify which part of the input JSON to use as the input for a state using the `InputPath` field. This allows you to filter the input data to only include relevant information for that state.
3. **Parameters**: You can pass parameters to a state using the `Parameters` field. This allows you to construct a new JSON object that includes both static values and dynamic values from the input. 
4. **State OutputPath**: After the state execution, you can specify which part of the output JSON to return as the output of the state using the `OutputPath` field. This allows you to filter the output data to only include relevant information for the next state or for the final output of the state machine.

### Flow for Lambda Variables execution:
```
State Input -> InputPath -> Parameters -> Lambda Function Execution -> OutputPath -> State Output
``` 
