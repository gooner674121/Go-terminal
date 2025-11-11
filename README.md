Step 1: Download Go Installer

Go to the official Go website:
https://go.dev/dl/

Download the Windows installer (.msi) for your system (usually Windows 64-bit).

Step 2: Install Go

Run the downloaded installer.

Follow the prompts:

Accept the license agreement.

Choose an installation path (default is usually fine):

C:\Go


Click Install and wait for the installation to finish.

Step 3: Add Go to Windows PATH (Usually Automatic)

The installer usually adds Go to the system PATH automatically.

To verify, open a new Command Prompt and type:

go version


You should see output similar to:

go version go1.25.4 windows/amd64


If not recognized, manually add:

C:\Go\bin


to the Windows PATH using Edit the system environment variables.

Step 4: Verify the Go Environment

Check the Go workspace path by typing:

go env


This shows key environment variables like GOPATH and GOROOT.

Step 5: Compile and Run Your First Go Program

Open a text editor and write a simple Go program:

package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}


Save it as hello.go.

Open Command Prompt in the folder containing hello.go.

Run the program directly using:

go run hello.go


Output:

Hello, world!


Optionally, build an executable:

go build hello.go
hello.exe


This produces hello.exe which you can run anytime.
