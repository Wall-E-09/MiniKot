// MiniKot to IL Generator
.assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }
.assembly all_features { .hash algorithm 0x00008004 .ver 0:0:0:0 }
.module all_features.exe

.class private auto ansi beforefieldinit Program extends [mscorlib]System.Object
{
  .method private hidebysig static void Main(string[] args) cil managed
  {
    .entrypoint
    .maxstack 8
    .locals init (
      [0] float64 __temp,
      [1] int32 MAX_VAL,
      [2] float64 PI,
      [3] bool isRunning,
      [4] string userName,
      [5] int32 counter,
      [6] float64 area,
      [7] float64 testCalc,
      [8] float64 f
    )

    ldc.i4 50
    stloc 1
    ldc.r8 3.1415
    stloc 2
    ldc.i4 1
    stloc 3
    ldstr ""
    stloc 4
    ldc.i4 0
    stloc 5
    ldc.r8 0.0
    stloc 6
    ldc.r8 0.0
    stloc 7
    ldc.r8 0.0
    stloc 8
    ldstr "Enter your name: "
    call void [mscorlib]System.Console::Write(string)
    call string [mscorlib]System.Console::ReadLine()
    stloc 4
    ldstr "Hello: "
    call void [mscorlib]System.Console::Write(string)
    ldloc 4
    call void [mscorlib]System.Console::WriteLine(string)
    ldstr "Enter start counter (int): "
    call void [mscorlib]System.Console::Write(string)
    call string [mscorlib]System.Console::ReadLine()
    call int32 [mscorlib]System.Int32::Parse(string)
    stloc 5
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
    stloc 7
    ldstr "Complex calc result (10+2*9-2): "
    call void [mscorlib]System.Console::Write(string)
    ldloc 7
    call void [mscorlib]System.Console::WriteLine(float64)
L_1:
    ldloc 3
    brfalse L_2
    ldloc 2
    ldloc 5
    conv.r8
    ldc.i4 2
    conv.r8
    call float64 [mscorlib]System.Math::Pow(float64, float64)
    mul
    stloc 6
    ldstr "Current Counter: "
    call void [mscorlib]System.Console::Write(string)
    ldloc 5
    call void [mscorlib]System.Console::WriteLine(int32)
    ldstr "Calculated Area: "
    call void [mscorlib]System.Console::Write(string)
    ldloc 6
    call void [mscorlib]System.Console::WriteLine(float64)
    ldloc 6
    ldc.r8 100.0
    clt
    ldc.i4.0
    ceq
    brfalse L_3
    ldstr "Area is Large"
    call void [mscorlib]System.Console::WriteLine(string)
    ldloc 6
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
    ldloc 6
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
    ldloc 5
    ldc.i4 5
    add
    stloc 5
    ldloc 5
    ldloc 1
    cgt
    brfalse L_9
    ldc.i4 0
    stloc 3
    br L_10
L_9:
L_10:
    ldloc 5
    ldc.i4 0
    cgt
    ldc.i4.0
    ceq
    brfalse L_11
    ldc.i4 0
    stloc 3
    br L_12
L_11:
L_12:
    br L_1
L_2:
    ldstr "Loop finished"
    call void [mscorlib]System.Console::Write(string)
    ret
  }
}
