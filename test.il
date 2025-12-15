// MiniKot to IL Generator
.assembly extern mscorlib { .publickeytoken = (B7 7A 5C 56 19 34 E0 89 ) .ver 4:0:0:0 }
.assembly test { .hash algorithm 0x00008004 .ver 0:0:0:0 }
.module test.exe

.class private auto ansi beforefieldinit Program extends [mscorlib]System.Object
{
  .method private hidebysig static void Main(string[] args) cil managed
  {
    .entrypoint
    .maxstack 8
    .locals init (
      [0] float64 __temp,
      [1] int32 a,
      [2] int32 b,
      [3] int32 c,
      [4] float64 powRes,
      [5] float64 mix,
      [6] int32 prio,
      [7] string name,
      [8] int32 score,
      [9] string result,
      [10] int32 i
    )

    ldstr "=== STARTING FINAL TEST ==="
    call void [mscorlib]System.Console::WriteLine(string)
    ldstr "[1] Math Check:"
    call void [mscorlib]System.Console::WriteLine(string)
    ldc.i4 2
    stloc 1
    ldc.i4 3
    stloc 2
    ldc.i4 2
    stloc 3
    ldloc 1
    conv.r8
    ldloc 2
    conv.r8
    ldloc 3
    conv.r8
    call float64 [mscorlib]System.Math::Pow(float64, float64)
    call float64 [mscorlib]System.Math::Pow(float64, float64)
    stloc 4
    ldstr "   2^3^2 (Expect 512): "
    call void [mscorlib]System.Console::Write(string)
    ldloc 4
    call void [mscorlib]System.Console::WriteLine(float64)
    ldc.i4 10
    ldc.r8 5.5
    stloc 0
    conv.r8
    ldloc 0
    add
    stloc 5
    ldstr "   10 + 5.5 (Expect 15.5): "
    call void [mscorlib]System.Console::Write(string)
    ldloc 5
    call void [mscorlib]System.Console::WriteLine(float64)
    ldc.i4 2
    ldc.i4 2
    ldc.i4 2
    mul
    add
    stloc 6
    ldstr "   2 + 2 * 2 (Expect 6): "
    call void [mscorlib]System.Console::Write(string)
    ldloc 6
    call void [mscorlib]System.Console::WriteLine(int32)
    ldstr ""
    call void [mscorlib]System.Console::WriteLine(string)
    ldstr "[2] String & Boxing Check:"
    call void [mscorlib]System.Console::WriteLine(string)
    ldstr "   Enter your name: "
    call void [mscorlib]System.Console::Write(string)
    call string [mscorlib]System.Console::ReadLine()
    stloc 7
    ldstr "   Enter your score (Int): "
    call void [mscorlib]System.Console::Write(string)
    call string [mscorlib]System.Console::ReadLine()
    call int32 [mscorlib]System.Int32::Parse(string)
    stloc 8
    ldstr "   User "
    ldloc 7
    call string [mscorlib]System.String::Concat(object, object)
    ldstr " has score: "
    call string [mscorlib]System.String::Concat(object, object)
    ldloc 8
    box [mscorlib]System.Int32
    call string [mscorlib]System.String::Concat(object, object)
    stloc 9
    ldloc 9
    call void [mscorlib]System.Console::WriteLine(string)
    ldstr ""
    call void [mscorlib]System.Console::WriteLine(string)
    ldstr "[3] Logic Check:"
    call void [mscorlib]System.Console::WriteLine(string)
    ldloc 8
    ldc.i4 50
    cgt
    brfalse L_1
    ldstr "   Result: PASS (Score > 50)"
    call void [mscorlib]System.Console::WriteLine(string)
    br L_2
L_1:
    ldstr "   Result: FAIL (Score <= 50)"
    call void [mscorlib]System.Console::WriteLine(string)
L_2:
    ldstr ""
    call void [mscorlib]System.Console::WriteLine(string)
    ldstr "[4] Loop Check:"
    call void [mscorlib]System.Console::WriteLine(string)
    ldc.i4 0
    stloc 10
L_3:
    ldloc 10
    ldc.i4 3
    clt
    brfalse L_4
    ldstr "   Iter: "
    call void [mscorlib]System.Console::Write(string)
    ldloc 10
    call void [mscorlib]System.Console::WriteLine(int32)
    ldloc 10
    ldc.i4 1
    add
    stloc 10
    br L_3
L_4:
    ldstr "=== TEST COMPLETED ==="
    call void [mscorlib]System.Console::WriteLine(string)
    ret
  }
}
