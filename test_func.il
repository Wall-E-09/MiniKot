// Generated IL Code for test_func
.assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }
.assembly test_func { .hash algorithm 0x00008004 .ver 0:0:0:0 }
.module test_func.exe

.class public auto ansi Program extends [mscorlib]System.Object
{

    // --- Global Fields ---
    .field public static int32 x
    .field public static int32 y
    .field public static int32 result

    // --- Functions ---
.method public static int32 sum(int32, int32) cil managed
{
    .maxstack 8
    .locals init (
        [0] float64 __temp,
        [1] int32 res
    )

    ldarg 0
    ldarg 1
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

        ldc.i4 10
        stsfld int32 Program::x
        ldc.i4 20
        stsfld int32 Program::y
        ldstr "Calling function sum(10, 20)..."
        call void [mscorlib]System.Console::WriteLine(string)
        ldsfld int32 Program::x
        ldsfld int32 Program::y
        call int32 Program::sum(int32, int32)
        stsfld int32 Program::result
        ldstr "Result: "
        call void [mscorlib]System.Console::WriteLine(string)
        ldsfld int32 Program::result
        call void [mscorlib]System.Console::WriteLine(int32)
        ret
    }
}
