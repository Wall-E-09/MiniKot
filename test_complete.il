// Generated IL Code for test_complete
.assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }
.assembly test_complete { .hash algorithm 0x00008004 .ver 0:0:0:0 }
.module test_complete.exe

.class public auto ansi Program extends [mscorlib]System.Object
{

    // --- Global Fields ---
    .field public static int32 globalVar
    .field public static float64 pi
    .field public static int32 x
    .field public static int32 y
    .field public static float64 powerTest
    .field public static float64 mixed
    .field public static int32 factRes
    .field public static int32 counter
    .field public static float64 z

    // --- Functions ---
.method public static int32 factorial(int32) cil managed
{
    .maxstack 8
    .locals init (
        [0] float64 __temp
    )

    ldarg 0
    ldc.i4 1
    cgt
    ldc.i4.0
    ceq
    brfalse L_1
    ldc.i4 1
    ret
    br L_2
L_1:
L_2:
    ldarg 0
    ldarg 0
    ldc.i4 1
    sub
    call int32 Program::factorial(int32)
    mul
    ret
}

.method public static float64 complexMath(float64, int32) cil managed
{
    .maxstack 8
    .locals init (
        [0] float64 __temp,
        [1] float64 res
    )

    ldarg 0
    ldc.i4 2
    conv.r8
    call float64 [mscorlib]System.Math::Pow(float64, float64)
    neg
    ldarg 1
    neg
    conv.r8
    add
    stloc 1
    ldloc 1
    ret
}

    // --- Main Method ---
    .method public static void Main(string[] args) cil managed
    {
        .entrypoint
        .maxstack 8
        .locals init (
            [0] float64 __temp
        )

        ldc.i4 100
        stsfld int32 Program::globalVar
        ldc.r8 3.14159
        stsfld float64 Program::pi
        ldstr "--- START TESTING ---"
        call void [mscorlib]System.Console::WriteLine(string)
        ldc.i4 5
        neg
        stsfld int32 Program::x
        ldsfld int32 Program::x
        neg
        ldc.i4 5
        sub
        neg
        stsfld int32 Program::y
        ldstr "Unary test (-(-(-5)-5)): "
        call void [mscorlib]System.Console::Write(string)
        ldsfld int32 Program::y
        call void [mscorlib]System.Console::WriteLine(int32)
        ldc.r8 2.0
        ldc.r8 3.0
        ldc.i4 2
        conv.r8
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        ldc.r8 2.0
        mul
        add
        stsfld float64 Program::powerTest
        ldstr "Power test (2+3^2*2): "
        call void [mscorlib]System.Console::Write(string)
        ldsfld float64 Program::powerTest
        call void [mscorlib]System.Console::WriteLine(float64)
        ldc.i4 10
        ldc.r8 0.5
        stloc 0
        conv.r8
        ldloc 0
        mul
        stsfld float64 Program::mixed
        ldstr "Mixed types (10 * 0.5): "
        call void [mscorlib]System.Console::Write(string)
        ldsfld float64 Program::mixed
        call void [mscorlib]System.Console::WriteLine(float64)
        ldstr "Global Var before func: "
        call void [mscorlib]System.Console::Write(string)
        ldsfld int32 Program::globalVar
        call void [mscorlib]System.Console::WriteLine(int32)
        ldc.i4 5
        call int32 Program::factorial(int32)
        stsfld int32 Program::factRes
        ldstr "Factorial of 5: "
        call void [mscorlib]System.Console::Write(string)
        ldsfld int32 Program::factRes
        call void [mscorlib]System.Console::WriteLine(int32)
        ldstr "Global Var after func: "
        call void [mscorlib]System.Console::Write(string)
        ldsfld int32 Program::globalVar
        call void [mscorlib]System.Console::WriteLine(int32)
        ldstr "Enter a negative number to start loop: "
        call void [mscorlib]System.Console::Write(string)
        call string [mscorlib]System.Console::ReadLine()
        call int32 [mscorlib]System.Int32::Parse(string)
        stsfld int32 Program::counter
        ldsfld int32 Program::counter
        ldc.i4 0
        clt
        ldc.i4.0
        ceq
        brfalse L_3
        ldstr "You entered a positive number or zero!"
        call void [mscorlib]System.Console::WriteLine(string)
        br L_4
    L_3:
        ldstr "Starting loop increment..."
        call void [mscorlib]System.Console::WriteLine(string)
    L_5:
        ldsfld int32 Program::counter
        ldc.i4 0
        clt
        brfalse L_6
        ldsfld int32 Program::counter
        ldc.i4 1
        add
        stsfld int32 Program::counter
        ldsfld int32 Program::counter
        ldc.i4 0
        ceq
        brfalse L_7
        ldstr "Counter reached ZERO!"
        call void [mscorlib]System.Console::WriteLine(string)
        br L_8
    L_7:
    L_8:
        br L_5
    L_6:
    L_4:
        ldc.r8 3.0
        ldc.i4 10
        neg
        call float64 Program::complexMath(float64, int32)
        stsfld float64 Program::z
        ldstr "Complex Function Result: "
        call void [mscorlib]System.Console::Write(string)
        ldsfld float64 Program::z
        call void [mscorlib]System.Console::WriteLine(float64)
        ldstr "--- END ---"
        call void [mscorlib]System.Console::WriteLine(string)
        ret
    }
}
