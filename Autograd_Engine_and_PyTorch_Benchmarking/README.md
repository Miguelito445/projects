# Automatic Differentiation Engine from Scratch and PyTorch Benchmarking

A small automatic differentiation (autograd) engine written in plain Python, checked against PyTorch, followed by a tiny neural network and a few PyTorch performance experiments.

## What the project is

The script `lab05.py` runs three parts in order:

1. **Autograd engine (`Value` class).** Each `Value` is a scalar that remembers how it was computed, so the program can build a computation graph. Supported operations: add, subtract, multiply, divide, power and ReLU. Calling `.backward()` sorts the graph topologically and applies the chain rule to compute gradients.
2. **Verification against PyTorch.** The same expression is computed with the custom engine and with PyTorch tensors. The gradients must match to within `1e-6`, otherwise an assertion fails.
3. **Training and benchmarking.**
   - A tiny neural network (2 inputs, 8 hidden ReLU units, 1 sigmoid output) is trained on the `make_moons` dataset with the Adam optimizer and binary cross-entropy loss. Training time is reported as the median of 5 runs.
   - Eager execution is compared with a traced model (`torch.jit.trace`) over 1,000 forward passes, and the result is saved as a bar chart.
   - A contiguous tensor is compared with a non-contiguous one (a transpose) to show the cost of memory layout.

## Goals

- Understand backpropagation by implementing it, not only by calling `loss.backward()`.
- Prove that the implementation is correct by comparing it with PyTorch.
- Practise a clean training loop and fair performance measurement.

## Results

- The custom gradients matched PyTorch within the `1e-6` tolerance.
- The included chart `execution_timings_comparison.png` shows the traced model slightly faster than eager execution (roughly 89 ms versus 94 ms for 1,000 runs on the machine used). Absolute numbers depend on your hardware.

## Files

- `lab05.py`: the full program.
- `execution_timings_comparison.png`: the benchmark chart produced by the program.
- `requirements.txt`: the package list provided with the lab.

## How to run

The program only needs these packages (NumPy is installed with them):

```bash
pip install torch scikit-learn matplotlib
python lab05.py
```

Notes:

- At the end, `lab05.py` saves the chart to a fixed Windows path (`output_plot_path`). Change that variable to a relative path such as `"execution_timings_comparison.png"` before running on another machine.
- `requirements.txt` contains more packages than the script uses (for example web and MLOps tools). The three packages above are enough to run it.

## What can be learned from it

- **How backpropagation works:** every operation stores a small local rule for its gradient, and the chain rule combines them from the output back to the inputs.
- **Computation graphs:** why gradients must be accumulated (`+=`) and why a topological order is needed.
- **Testing numerical code:** comparing against a trusted library with a tolerance.
- **A basic training loop:** zero the gradients, forward pass, loss, backward pass, optimizer step.
- **Benchmarking correctly:** warm-up runs, many repetitions and the median instead of a single measurement.
- **Memory layout:** contiguous versus non-contiguous tensors, and why this can affect speed.
