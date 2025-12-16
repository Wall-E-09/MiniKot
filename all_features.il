// Generated IL Code for all_features
.assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }
.assembly all_features { .hash algorithm 0x00008004 .ver 0:0:0:0 }
.module all_features.exe

.class public auto ansi Program extends [mscorlib]System.Object
{

    // --- Global Fields ---
    .field public static int32 MAX_VAL
    .field public static float64 PI
    .field public static bool isRunning
    .field public static string userName
    .field public static int32 counter
    .field public static float64 area
    .field public static float64 testCalc
    .field public static float64 f
    .field public static int32 e

    // --- Functions ---
.method public static float64 sum(float64, int32) cil managed
{
    .maxstack 8
    .locals init (
        [0] float64 __temp,
        [1] float64 res
    )

    ldarg 0
    ldarg 1
    conv.r8
    add
    stloc 1
    ldstr "Function result: "
    call void [mscorlib]System.Console::Write(string)
    ldloc 1
    call void [mscorlib]System.Console::WriteLine(float64)
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

        ldc.i4 50
        stsfld int32 Program::MAX_VAL
        ldc.r8 3.1415
        stsfld float64 Program::PI
        ldc.i4 1
        stsfld bool Program::isRunning
        ldstr ""
        stsfld string Program::userName
        ldc.i4 0
        stsfld int32 Program::counter
        ldc.r8 0.0
        stsfld float64 Program::area
        ldc.r8 0.0
        stsfld float64 Program::testCalc
        ldc.r8 0.0
        stsfld float64 Program::f
        ldc.i4 0
        stsfld int32 Program::e
        ldc.i4 2
        conv.r8
        ldc.i4 3
        conv.r8
        ldc.i4 2
        conv.r8
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        conv.i4
        stsfld int32 Program::e
        ldsfld int32 Program::e
        call void [mscorlib]System.Console::WriteLine(int32)
        ldstr "Enter your name: "
        call void [mscorlib]System.Console::Write(string)
        call string [mscorlib]System.Console::ReadLine()
        stsfld string Program::userName
        ldstr "Hello: "
        call void [mscorlib]System.Console::Write(string)
        ldsfld string Program::userName
        call void [mscorlib]System.Console::WriteLine(string)
        ldstr "Enter start counter (int): "
        call void [mscorlib]System.Console::Write(string)
        call string [mscorlib]System.Console::ReadLine()
        call int32 [mscorlib]System.Int32::Parse(string)
        stsfld int32 Program::counter
        ldc.r8 10.0
        ldc.r8 2.0
        ldc.r8 3.0
        ldc.i4 2
        conv.r8
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        mul
        add
        ldc.r8 4.0
        ldc.r8 2.0
        div
        sub
        stsfld float64 Program::testCalc
        ldstr "Complex calc result (10+2*9-2): "
        call void [mscorlib]System.Console::Write(string)
        ldsfld float64 Program::testCalc
        call void [mscorlib]System.Console::WriteLine(float64)
    L_1:
        ldsfld bool Program::isRunning
        brfalse L_2
        ldsfld float64 Program::PI
        ldsfld int32 Program::counter
        conv.r8
        ldc.i4 2
        conv.r8
        call float64 [mscorlib]System.Math::Pow(float64, float64)
        mul
        stsfld float64 Program::area
        ldstr "Current Counter: "
        call void [mscorlib]System.Console::Write(string)
        ldsfld int32 Program::counter
        call void [mscorlib]System.Console::WriteLine(int32)
        ldstr "Calculated Area: "
        call void [mscorlib]System.Console::Write(string)
        ldsfld float64 Program::area
        call void [mscorlib]System.Console::WriteLine(float64)
        ldsfld float64 Program::area
        ldc.r8 100.0
        clt
        ldc.i4.0
        ceq
        brfalse L_3
        ldstr "Area is Large"
        call void [mscorlib]System.Console::WriteLine(string)
        ldsfld float64 Program::area
        ldc.r8 314.15
        ceq
        brfalse L_5
        ldstr "Exact Match with 314.15"
        call void [mscorlib]System.Console::WriteLine(string)
        br L_6
    L_5:
    L_6:
        br L_4
    L_3:
        ldstr "Area is Small"
        call void [mscorlib]System.Console::WriteLine(string)
        ldsfld float64 Program::area
        ldc.r8 0.0
        ceq
        ldc.i4.0
        ceq
        brfalse L_7
        ldstr "Area is not Zero"
        call void [mscorlib]System.Console::WriteLine(string)
        br L_8
    L_7:
    L_8:
    L_4:
        ldsfld int32 Program::counter
        ldc.i4 5
        add
        stsfld int32 Program::counter
        ldsfld int32 Program::counter
        ldsfld int32 Program::MAX_VAL
        cgt
        brfalse L_9
        ldc.i4 0
        stsfld bool Program::isRunning
        br L_10
    L_9:
    L_10:
        ldsfld int32 Program::counter
        ldc.i4 0
        cgt
        ldc.i4.0
        ceq
        brfalse L_11
        ldc.i4 0
        stsfld bool Program::isRunning
        br L_12
    L_11:
    L_12:
        br L_1
    L_2:
        ldc.r8 3.5
        ldc.i4 2
        call float64 Program::sum(float64, int32)
        stsfld float64 Program::f
        ldstr "Loop finished"
        call void [mscorlib]System.Console::Write(string)
        ret
    }
}
