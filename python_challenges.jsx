import { useState } from "react";

const challenges = [
  {
    id: 1,
    level: "🌱 Nivel 1",
    title: "Calculadora de propinas",
    description: "Escribe un programa que pida al usuario el total de una cuenta de restaurante y calcule una propina del 15%, 18% y 20%.",
    hint: "Usa `input()` para pedir datos y recuerda convertir el texto a número con `float()`.",
    example: `total = float(input("¿Cuánto fue la cuenta? $"))
propina_15 = total * 0.15
print(f"Propina 15%: ${propina_15:.2f}")`,
    xp: 10,
  },
  {
    id: 2,
    level: "🌱 Nivel 2",
    title: "Adivina el número",
    description: "Genera un número aleatorio entre 1 y 10. El usuario tiene 3 intentos para adivinarlo. Indica si el número es mayor o menor.",
    hint: "Usa `import random` y `random.randint(1, 10)`. Usa un bucle `for` o `while`.",
    example: `import random
numero = random.randint(1, 10)`,
    xp: 20,
  },
  {
    id: 3,
    level: "🌿 Nivel 3",
    title: "Contador de vocales",
    description: "Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) contiene, sin importar mayúsculas o minúsculas.",
    hint: "Usa `.lower()` para ignorar mayúsculas y un bucle `for` para recorrer cada letra.",
    example: `frase = input("Escribe una frase: ").lower()
vocales = "aeiou"`,
    xp: 30,
  },
  {
    id: 4,
    level: "🌿 Nivel 4",
    title: "Lista de tareas",
    description: "Crea un programa de consola que permita: agregar tareas, ver todas las tareas, y marcar una tarea como completada. Usa un menú con opciones.",
    hint: "Usa una lista `[]` para guardar las tareas. Usa un bucle `while True` con un menú de opciones.",
    example: `tareas = []
while True:
    print("1. Agregar  2. Ver  3. Completar  4. Salir")
    opcion = input("Elige: ")`,
    xp: 50,
  },
  {
    id: 5,
    level: "🌳 Nivel 5",
    title: "Analizador de texto",
    description: "Dado un texto, calcula: número de palabras, palabra más frecuente, y número de oraciones. El texto puede ser ingresado por el usuario.",
    hint: "Usa `.split()` para separar palabras y un diccionario `{}` para contar frecuencias.",
    example: `from collections import Counter
texto = input("Ingresa un texto: ")
palabras = texto.lower().split()
conteo = Counter(palabras)`,
    xp: 75,
  },
];

export default function ChallengeTracker() {
  const [completed, setCompleted] = useState({});
  const [showHint, setShowHint] = useState({});
  const [showExample, setShowExample] = useState({});
  const [current, setCurrent] = useState(1);

  const totalXP = challenges.reduce((sum, c) => completed[c.id] ? sum + c.xp : sum, 0);
  const maxXP = challenges.reduce((sum, c) => sum + c.xp, 0);

  const toggle = (id) => {
    setCompleted(prev => {
      const next = { ...prev, [id]: !prev[id] };
      if (!prev[id]) {
        const nextChallenge = challenges.find(c => c.id === id + 1);
        if (nextChallenge) setCurrent(nextChallenge.id);
      }
      return next;
    });
  };

  return (
    <div style={{ fontFamily: "'Segoe UI', sans-serif", background: "#0f172a", minHeight: "100vh", padding: "24px", color: "#e2e8f0" }}>
      <div style={{ maxWidth: 680, margin: "0 auto" }}>
        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: 32 }}>
          <h1 style={{ fontSize: 28, fontWeight: 800, color: "#7dd3fc", margin: 0 }}>🐍 Desafíos Python</h1>
          <p style={{ color: "#94a3b8", marginTop: 8 }}>Principiante → Intermedio</p>
          {/* XP Bar */}
          <div style={{ marginTop: 16, background: "#1e293b", borderRadius: 99, height: 14, overflow: "hidden" }}>
            <div style={{ height: "100%", width: `${(totalXP / maxXP) * 100}%`, background: "linear-gradient(90deg, #38bdf8, #818cf8)", borderRadius: 99, transition: "width 0.4s ease" }} />
          </div>
          <p style={{ color: "#7dd3fc", marginTop: 6, fontWeight: 700 }}>{totalXP} / {maxXP} XP</p>
        </div>

        {/* Challenges */}
        {challenges.map((c) => {
          const isCompleted = completed[c.id];
          const isCurrent = current === c.id;
          const isLocked = c.id > current && !isCompleted;

          return (
            <div key={c.id} style={{
              background: isCompleted ? "#134e2a" : isCurrent ? "#1e293b" : "#151e2d",
              border: `2px solid ${isCompleted ? "#22c55e" : isCurrent ? "#38bdf8" : "#1e293b"}`,
              borderRadius: 16, padding: 20, marginBottom: 16,
              opacity: isLocked ? 0.5 : 1,
              transition: "all 0.3s"
            }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
                <div style={{ flex: 1 }}>
                  <span style={{ fontSize: 12, color: "#94a3b8", fontWeight: 600 }}>{c.level}</span>
                  <h2 style={{ margin: "4px 0 8px", fontSize: 18, fontWeight: 700, color: isCompleted ? "#4ade80" : "#e2e8f0" }}>
                    {isLocked ? "🔒 " : isCompleted ? "✅ " : "⚡ "}{c.title}
                  </h2>
                  <p style={{ margin: 0, color: "#94a3b8", fontSize: 14, lineHeight: 1.6 }}>{c.description}</p>
                </div>
                <span style={{ marginLeft: 12, background: "#7dd3fc22", color: "#7dd3fc", padding: "4px 10px", borderRadius: 99, fontSize: 13, fontWeight: 700, whiteSpace: "nowrap" }}>+{c.xp} XP</span>
              </div>

              {!isLocked && (
                <div style={{ marginTop: 14, display: "flex", gap: 8, flexWrap: "wrap" }}>
                  <button onClick={() => setShowHint(p => ({ ...p, [c.id]: !p[c.id] }))}
                    style={{ background: "#1e3a5f", color: "#93c5fd", border: "none", borderRadius: 8, padding: "6px 14px", cursor: "pointer", fontSize: 13 }}>
                    {showHint[c.id] ? "Ocultar pista" : "💡 Ver pista"}
                  </button>
                  <button onClick={() => setShowExample(p => ({ ...p, [c.id]: !p[c.id] }))}
                    style={{ background: "#2d1f5e", color: "#c4b5fd", border: "none", borderRadius: 8, padding: "6px 14px", cursor: "pointer", fontSize: 13 }}>
                    {showExample[c.id] ? "Ocultar código" : "📄 Ver código base"}
                  </button>
                  <button onClick={() => toggle(c.id)}
                    style={{ background: isCompleted ? "#14532d" : "#164e63", color: isCompleted ? "#4ade80" : "#38bdf8", border: `1px solid ${isCompleted ? "#22c55e" : "#38bdf8"}`, borderRadius: 8, padding: "6px 14px", cursor: "pointer", fontSize: 13, marginLeft: "auto" }}>
                    {isCompleted ? "✅ Completado" : "Marcar como completado"}
                  </button>
                </div>
              )}

              {showHint[c.id] && (
                <div style={{ marginTop: 12, background: "#1e3a5f", borderRadius: 10, padding: 14, color: "#93c5fd", fontSize: 13 }}>
                  💡 {c.hint}
                </div>
              )}
              {showExample[c.id] && (
                <pre style={{ marginTop: 12, background: "#0f172a", borderRadius: 10, padding: 14, color: "#a5f3fc", fontSize: 13, overflowX: "auto", border: "1px solid #1e293b" }}>
                  {c.example}
                </pre>
              )}
            </div>
          );
        })}

        <p style={{ textAlign: "center", color: "#475569", fontSize: 13, marginTop: 24 }}>
          ¡Completa cada desafío antes de desbloquear el siguiente! 🚀
        </p>
      </div>
    </div>
  );
}
