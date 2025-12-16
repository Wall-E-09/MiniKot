// MiniKot to IL Generator
.assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }
.assembly test_semantic { .hash algorithm 0x00008004 .ver 0:0:0:0 }
.module test_semantic.exe

.class private auto ansi beforefieldinit Program extends [mscorlib]System.Object
{
  .method private hidebysig static void Main(string[] args) cil managed
  {
    .entrypoint
    .maxstack 8
    .locals init (
      [0] float64 __temp,
      [1] int32 counter,
      [2] float64 PI,
      [3] float64 radius,
      [4] float64 area,
      [5] int32 y,
      [6] int32 h
    )

    ldc.i4 0
    stloc 1
    ldc.r8 3.14
    stloc 2
    ldc.r8 0.0
    stloc 3
    ldc.r8 0.0
    stloc 4
    ldc.i4 0
    stloc 5
    ldc.i4 0
    stloc 6
    ldstr "Enter radius: "
    call void [mscorlib]System.Console::Write(string)
    call string [mscorlib]System.Console::ReadLine()
    call float64 [mscorlib]System.Double::Parse(string)
    stloc 3
    ldloc 2
    ldloc 3
    ldc.i4 2
    conv.r8
    call float64 [mscorlib]System.Math::Pow(float64, float64)
    mul
    stloc 4
    ldloc 4
    ldc.r8 100.0
    cgt
    brfalse L_1
    ldstr "Big Area"
    call void [mscorlib]System.Console::Write(string)
    ldloc 4
    call void [mscorlib]System.Console::Write(float64)
    br L_2
L_1:
    ldstr "Small Area"
    call void [mscorlib]System.Console::Write(string)
L_2:
L_3:
    ldloc 1
    ldc.i4 3
    clt
    brfalse L_4
    ldloc 1
    call void [mscorlib]System.Console::Write(int32)
    ldloc 1
    ldc.i4 1
    add
    stloc 1
    br L_3
L_4:
    stloc 5
    ret
  }
}
