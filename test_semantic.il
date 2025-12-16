// Generated IL Code for test_semantic
.assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }
.assembly test_semantic { .hash algorithm 0x00008004 .ver 0:0:0:0 }
.module test_semantic.exe

.class public auto ansi Program extends [mscorlib]System.Object
{

    // --- Global Fields ---
    .field public static int32 counter
    .field public static float64 PI
    .field public static float64 radius
    .field public static float64 area
    .field public static int32 y
    .field public static float64 h

    // --- Functions ---
.method public static int32 sum(int32, int32) cil managed
{
    .maxstack 8
    .locals init (
        [0] float64 __temp
    )

    ldarg 0
    ldarg 1
    add
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

        ldc.i4 0
        stsfld int32 Program::counter
        ldc.r8 3.14
        stsfld float64 Program::PI
        ldc.r8 0.0
        stsfld float64 Program::radius
        ldc.r8 0.0
        stsfld float64 Program::area
        ldc.i4 0
        stsfld int32 Program::y
        ldc.i4 0
        conv.r8
        stsfld float64 Program::h
        ldstr "Enter radius: "
        call void [mscorlib]System.Console::Write(string)
        call string [mscorlib]System.Console::ReadLine()
        call float64 [mscorlib]System.Double::Parse(string)
        stsfld float64 Program::radius
        ldsfld float64 Program::PI
        ldsfld float64 Program::radius
        ldc.i4 2
        conv.r8
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        mul
        stsfld float64 Program::area
        ldsfld float64 Program::area
        ldc.r8 100.0
        cgt
        brfalse L_1
        ldstr "Big Area"
        call void [mscorlib]System.Console::WriteLine(string)
        ldsfld float64 Program::area
        call void [mscorlib]System.Console::WriteLine(float64)
        br L_2
    L_1:
        ldstr "Small Area"
        call void [mscorlib]System.Console::WriteLine(string)
    L_2:
    L_3:
        ldsfld int32 Program::counter
        ldc.i4 3
        clt
        brfalse L_4
        ldsfld int32 Program::counter
        call void [mscorlib]System.Console::WriteLine(int32)
        ldsfld int32 Program::counter
        ldc.i4 1
        add
        stsfld int32 Program::counter
        br L_3
    L_4:
        ldc.i4 2
        ldc.i4 3
        call int32 Program::sum(int32, int32)
        stsfld int32 Program::y
        ldsfld int32 Program::y
        call void [mscorlib]System.Console::WriteLine(int32)
        ldc.i4 2
        conv.r8
        ldc.i4 3
        conv.r8
        ldc.r8 2.5
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        stsfld float64 Program::h
        ldsfld float64 Program::h
        call void [mscorlib]System.Console::WriteLine(float64)
        ret
    }
}
