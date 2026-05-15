html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contabilidade Industrial — v7.0</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<script>
tailwind.config = {
  theme: {
    extend: {
      colors: {
        navy: { 900:'#0a0f1e', 800:'#111827', 700:'#1a2438', 600:'#1e2d47', 500:'#243558' },
        gold: { 400:'#f4c842', 500:'#e8b830', 600:'#d4a020' },
        emerald2: { 400:'#34d399', 500:'#10b981' }
      },
      fontFamily: { playfair:['Playfair Display','serif'], inter:['Inter','sans-serif'], mono:['JetBrains Mono','monospace'] }
    }
  }
}
</script>
<style>
*{box-sizing:border-box}
body{background:#0a0f1e;color:#e2e8f0;font-family:'Inter',sans-serif;margin:0;padding:0}
.tab-content{display:none}.tab-content.active{display:block}
.sticky-nav{position:sticky;top:0;z-index:100;background:linear-gradient(135deg,#111827,#1a2438);border-bottom:2px solid #e8b830;box-shadow:0 4px 20px rgba(0,0,0,.5)}
.nav-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:0;overflow-x:auto;scrollbar-width:none}
.nav-inner::-webkit-scrollbar{display:none}
.nav-tab{padding:14px 18px;font-size:.8rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;cursor:pointer;border:none;background:transparent;color:#94a3b8;transition:all .3s;white-space:nowrap;border-bottom:3px solid transparent;margin-bottom:-2px}
.nav-tab:hover{color:#f4c842;background:rgba(244,200,66,.07)}
.nav-tab.active{color:#f4c842;border-bottom-color:#f4c842;background:rgba(244,200,66,.1)}
.page{max-width:1200px;margin:0 auto;padding:32px 20px}
.card{background:linear-gradient(135deg,#111827,#1a2438);border:1px solid #1e2d47;border-radius:16px;padding:24px;margin-bottom:20px}
.card-gold{border-color:rgba(244,200,66,.4);background:linear-gradient(135deg,rgba(244,200,66,.07),rgba(244,200,66,.03))}
.card-green{border-color:rgba(52,211,153,.3);background:rgba(52,211,153,.05)}
.card-red{border-color:rgba(239,68,68,.3);background:rgba(239,68,68,.05)}
.section-title{font-family:'Playfair Display',serif;font-size:1.6rem;color:#f4c842;margin-bottom:20px}
.badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:.75rem;font-weight:600}
.badge-gold{background:rgba(244,200,66,.2);color:#f4c842;border:1px solid rgba(244,200,66,.4)}
.badge-blue{background:rgba(96,165,250,.15);color:#93c5fd;border:1px solid rgba(96,165,250,.3)}
.badge-green{background:rgba(52,211,153,.15);color:#6ee7b7;border:1px solid rgba(52,211,153,.3)}
.badge-red{background:rgba(239,68,68,.15);color:#fca5a5;border:1px solid rgba(239,68,68,.3)}
.btn{padding:10px 22px;border-radius:10px;font-weight:600;font-size:.85rem;cursor:pointer;border:none;transition:all .25s;letter-spacing:.03em}
.btn-gold{background:linear-gradient(135deg,#e8b830,#d4a020);color:#0a0f1e}
.btn-gold:hover{background:linear-gradient(135deg,#f4c842,#e8b830);transform:translateY(-1px);box-shadow:0 4px 15px rgba(244,200,66,.3)}
.btn-outline{background:transparent;border:1px solid #e8b830;color:#e8b830}
.btn-outline:hover{background:rgba(232,184,48,.1)}
.btn-green{background:linear-gradient(135deg,#10b981,#059669);color:#fff}
.btn-green:hover{background:linear-gradient(135deg,#34d399,#10b981);transform:translateY(-1px)}
.btn-red{background:linear-gradient(135deg,#ef4444,#dc2626);color:#fff}
.btn-sm{padding:6px 14px;font-size:.78rem}
table.data-table{width:100%;border-collapse:collapse;font-size:.88rem}
table.data-table th{background:rgba(244,200,66,.15);color:#f4c842;padding:10px 14px;text-align:left;border-bottom:2px solid rgba(244,200,66,.3);font-size:.8rem;letter-spacing:.05em}
table.data-table td{padding:9px 14px;border-bottom:1px solid rgba(255,255,255,.06);color:#cbd5e1}
table.data-table tr:hover td{background:rgba(255,255,255,.03)}
.razonete{background:#111827;border:1px solid #243558;border-radius:12px;overflow:hidden;margin-bottom:16px}
.raz-name{background:linear-gradient(135deg,#1a2438,#243558);padding:10px 16px;font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#f4c842;text-align:center;border-bottom:1px solid #243558}
.raz-grid{display:grid;grid-template-columns:1fr 1fr;gap:0}
.raz-col-header{background:rgba(244,200,66,.1);padding:6px;text-align:center;font-size:.75rem;font-weight:700;color:#94a3b8;letter-spacing:.05em;border-bottom:1px solid #243558}
.raz-debit{border-right:1px solid #243558}
.raz-entry{display:flex;justify-content:space-between;align-items:center;padding:5px 10px;border-bottom:1px solid rgba(255,255,255,.04);font-family:'JetBrains Mono',monospace;font-size:.78rem}
.raz-entry .ref{color:#64748b;font-size:.7rem;margin-right:6px}
.raz-entry .val{color:#e2e8f0}
.raz-entry.si .val{color:#f4c842}
.raz-entry.student input{background:#0a0f1e;border:1px solid #243558;border-radius:4px;color:#e2e8f0;font-family:'JetBrains Mono',monospace;font-size:.78rem;padding:2px 6px;width:90px;text-align:right}
.raz-entry.student input:focus{outline:none;border-color:#e8b830;box-shadow:0 0 0 2px rgba(232,184,48,.2)}
.raz-entry.saldo{background:rgba(244,200,66,.07);border-top:2px solid rgba(244,200,66,.3)}
.raz-entry.saldo .val{color:#f4c842;font-weight:700}
.raz-entry.correct{background:rgba(52,211,153,.08)}
.raz-entry.wrong{background:rgba(239,68,68,.08)}
.step-card{border:1px solid #243558;border-radius:12px;padding:20px;margin-bottom:12px;background:#111827}
.step-card.active-step{border-color:rgba(244,200,66,.5);background:rgba(244,200,66,.05)}
.je-line{display:grid;grid-template-columns:40px 220px 1fr 1fr;gap:8px;padding:5px 0;font-family:'JetBrains Mono',monospace;font-size:.82rem;align-items:center;border-bottom:1px solid rgba(255,255,255,.05)}
.je-line .acct-debit{color:#93c5fd;padding-left:0}
.je-line .acct-credit{color:#fca5a5;padding-left:28px}
.je-line .val-debit{color:#93c5fd;text-align:right}
.je-line .val-credit{color:#fca5a5;text-align:right}
.quiz-option{padding:12px 18px;border-radius:10px;border:1px solid #243558;background:#111827;cursor:pointer;margin-bottom:8px;transition:all .2s;text-align:left;width:100%;color:#e2e8f0;font-size:.9rem}
.quiz-option:hover{border-color:#e8b830;background:rgba(244,200,66,.07);color:#f4c842}
.quiz-option.selected{border-color:#f4c842;background:rgba(244,200,66,.12);color:#f4c842}
.quiz-option.correct{border-color:#10b981;background:rgba(16,185,129,.1);color:#6ee7b7}
.quiz-option.wrong{border-color:#ef4444;background:rgba(239,68,68,.1);color:#fca5a5}
.bp-section{margin-bottom:20px}
.bp-row{display:flex;justify-content:space-between;padding:6px 12px;border-bottom:1px solid rgba(255,255,255,.04);font-size:.87rem}
.bp-row.header{background:rgba(244,200,66,.1);font-weight:700;color:#f4c842;font-size:.8rem;letter-spacing:.05em}
.bp-row.subtotal{border-top:1px solid rgba(244,200,66,.3);font-weight:600;color:#f4c842}
.bp-row.total{background:rgba(244,200,66,.15);font-weight:700;color:#f4c842;font-size:.95rem;border-top:2px solid #e8b830}
.equiv-input{background:#0a0f1e;border:1px solid #243558;border-radius:6px;color:#e2e8f0;font-family:'JetBrains Mono',monospace;padding:6px 10px;width:80px;text-align:center;font-size:.9rem}
.equiv-input:focus{outline:none;border-color:#e8b830;box-shadow:0 0 0 2px rgba(232,184,48,.2)}
.cpp-input{background:#0a0f1e;border:1px solid #243558;border-radius:6px;color:#e2e8f0;font-family:'JetBrains Mono',monospace;padding:6px 10px;width:110px;text-align:right;font-size:.9rem}
.cpp-input:focus{outline:none;border-color:#e8b830;box-shadow:0 0 0 2px rgba(232,184,48,.2)}
.formula-box{background:#0a0f1e;border:1px solid rgba(244,200,66,.3);border-radius:10px;padding:16px;font-family:'JetBrains Mono',monospace;font-size:.9rem;color:#f4c842;text-align:center;letter-spacing:.05em}
.highlight{color:#f4c842;font-weight:700}
.info-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.info-card{background:#111827;border:1px solid #1e2d47;border-radius:10px;padding:16px;text-align:center}
.info-card .label{font-size:.75rem;color:#64748b;letter-spacing:.05em;text-transform:uppercase;margin-bottom:6px}
.info-card .value{font-size:1.4rem;font-weight:700;color:#f4c842;font-family:'JetBrains Mono',monospace}
.info-card .sub{font-size:.75rem;color:#94a3b8;margin-top:4px}
.msg{padding:12px 18px;border-radius:8px;font-size:.88rem;margin-top:12px}
.msg-success{background:rgba(16,185,129,.12);border:1px solid rgba(16,185,129,.3);color:#6ee7b7}
.msg-error{background:rgba(239,68,68,.12);border:1px solid rgba(239,68,68,.3);color:#fca5a5}
.msg-info{background:rgba(96,165,250,.12);border:1px solid rgba(96,165,250,.3);color:#93c5fd}
.progress-bar{background:#1e2d47;border-radius:99px;height:8px;overflow:hidden;margin-top:6px}
.progress-fill{background:linear-gradient(90deg,#e8b830,#f4c842);height:100%;transition:width .4s ease}
.tag{display:inline-flex;align-items:center;gap:4px;padding:3px 8px;border-radius:6px;font-size:.72rem;font-weight:600}
.tag-d{background:rgba(96,165,250,.15);color:#93c5fd}
.tag-c{background:rgba(252,165,165,.15);color:#fca5a5}
hr.gold{border:none;border-top:1px solid rgba(244,200,66,.2);margin:20px 0}
</style>
</head>
<body>

<nav class="sticky-nav">
  <div class="nav-inner" id="navInner">
    <button class="nav-tab active" onclick="showTab('enunciado')" id="navBtn-enunciado">📋 Enunciado</button>
    <button class="nav-tab" onclick="showTab('equiv')" id="navBtn-equiv">⚖️ Equiv. Produção</button>
    <button class="nav-tab" onclick="showTab('cpp')" id="navBtn-cpp">🏭 CPP</button>
    <button class="nav-tab" onclick="showTab('razonetes')" id="navBtn-razonetes">📒 Razonetes</button>
    <button class="nav-tab" onclick="showTab('balanco')" id="navBtn-balanco">📊 Balanço</button>
    <button class="nav-tab" onclick="showTab('resolucao')" id="navBtn-resolucao">📖 Resolução</button>
    <button class="nav-tab" onclick="showTab('quiz')" id="navBtn-quiz">🎯 Quiz</button>
  </div>
</nav>

<!-- ==================== TAB: ENUNCIADO ==================== -->
<div id="tab-enunciado" class="tab-content active">
<div class="page">
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:28px">
    <div style="background:linear-gradient(135deg,#e8b830,#d4a020);width:50px;height:50px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;flex-shrink:0">🏭</div>
    <div>
      <div style="font-size:.8rem;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px">Contabilidade Industrial</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.8rem;color:#f4c842;line-height:1">Exercício Completo — v7.0</div>
    </div>
  </div>

  <div class="card card-gold" style="margin-bottom:24px">
    <div class="section-title" style="margin-bottom:12px">📦 Dados de Compras e Custos</div>
    <div class="info-grid">
      <div class="info-card"><div class="label">Compra MP</div><div class="value" style="font-size:1.1rem">500 kg</div><div class="sub">Valor R$13.900 | IPI R$1.000 | ICMS R$2.900</div></div>
      <div class="info-card"><div class="label">Energia do Período</div><div class="value" style="font-size:1.1rem">R$1.400</div><div class="sub">80% fábrica · 20% escritório</div></div>
      <div class="info-card"><div class="label">CIF do Período</div><div class="value" style="font-size:1.1rem">R$4.200</div><div class="sub">Custos Indiretos de Fabricação</div></div>
      <div class="info-card"><div class="label">CPP Equivalente</div><div class="value" style="font-size:1.1rem">1.530 und</div><div class="sub">Unidades equivalentes de produção</div></div>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px">
    <div class="card">
      <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:16px;letter-spacing:.05em">⚙️ PARÂMETROS TÉCNICOS</div>
      <table class="data-table">
        <tr><th>Item</th><th>Custo Unitário</th><th>Rendimento</th></tr>
        <tr><td>Mão de Obra Direta</td><td class="highlight">R$ 15,00/h</td><td>2 h → 1 unidade</td></tr>
        <tr><td>Matéria Prima</td><td class="highlight">R$ 20,00/kg</td><td>1 kg → 5 unidades</td></tr>
        <tr><td>Maquinário</td><td class="highlight">10% a.a.</td><td>R$ 5.000/mês</td></tr>
        <tr><td>Imóveis</td><td class="highlight">4% a.a.</td><td>R$ 4.000/mês</td></tr>
      </table>
    </div>
    <div class="card">
      <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:16px;letter-spacing:.05em">📦 ESTOQUES INICIAIS</div>
      <table class="data-table">
        <tr><th>Estoque</th><th>Quantidade</th><th>Valor</th></tr>
        <tr><td>Prod. Acabados</td><td>1.060 und</td><td>R$ 44.536,00</td></tr>
        <tr><td>Prod. Elaboração</td><td>400 und @ 30%</td><td>R$ 5.203,20</td></tr>
        <tr><td>Matéria Prima</td><td>—</td><td>R$ 4.000,00</td></tr>
      </table>
    </div>
  </div>

  <div class="card">
    <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:16px;letter-spacing:.05em">🏷️ MOVIMENTAÇÃO DO PERÍODO</div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">
      <div style="background:#0a0f1e;border-radius:10px;padding:16px;border:1px solid #243558">
        <div style="font-size:.75rem;color:#64748b;margin-bottom:8px">PRODUÇÃO</div>
        <div style="font-size:.85rem;color:#e2e8f0">400 und em elaboração (30%) <span style="color:#34d399">→ concluídas</span></div>
        <div style="margin-top:8px;font-size:.85rem;color:#e2e8f0">500 und iniciadas e produzidas <span style="color:#94a3b8">até 50%</span></div>
      </div>
      <div style="background:#0a0f1e;border-radius:10px;padding:16px;border:1px solid #243558">
        <div style="font-size:.75rem;color:#64748b;margin-bottom:8px">VENDAS</div>
        <div style="font-size:1.3rem;font-weight:700;color:#f4c842;font-family:'JetBrains Mono',monospace">2.000 und</div>
        <div style="font-size:.8rem;color:#94a3b8;margin-top:4px">R$ 570.000 + IPI R$ 46.000</div>
        <div style="font-size:.8rem;color:#94a3b8">ICMS R$ 88.000 (por dentro)</div>
      </div>
      <div style="background:#0a0f1e;border-radius:10px;padding:16px;border:1px solid #243558">
        <div style="font-size:.75rem;color:#64748b;margin-bottom:8px">POLÍTICA COMERCIAL</div>
        <div style="font-size:.85rem;color:#e2e8f0">Compras: <span style="color:#f4c842">a prazo</span></div>
        <div style="margin-top:8px;font-size:.85rem;color:#e2e8f0">Vendas: <span style="color:#f4c842">a prazo</span></div>
      </div>
    </div>
  </div>

  <div class="card card-gold">
    <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:16px;letter-spacing:.05em">🏦 SALDOS INICIAIS DO BALANÇO</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
      <div>
        <div style="font-size:.78rem;font-weight:700;color:#94a3b8;margin-bottom:10px;text-transform:uppercase;letter-spacing:.05em">ATIVO</div>
        <table class="data-table">
          <tr><td>BCM</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">195.760,00</td></tr>
          <tr><td>Clientes</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">1.184.368,00</td></tr>
          <tr><td>Estoque MP</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">4.000,00</td></tr>
          <tr><td>Est. Elaboração</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">5.203,20</td></tr>
          <tr><td>Est. Acabados</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">44.536,00</td></tr>
          <tr><td>Máquinas</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">600.000,00</td></tr>
          <tr><td>(-) Dep. Acum. Máq.</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#fca5a5">(20.000,00)</td></tr>
          <tr><td>Imóveis</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">1.200.000,00</td></tr>
          <tr><td>(-) Dep. Acum. Imóv.</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#fca5a5">(16.000,00)</td></tr>
          <tr style="font-weight:700;border-top:2px solid rgba(244,200,66,.3)"><td style="color:#f4c842">TOTAL ATIVO</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#f4c842">3.197.867,20</td></tr>
        </table>
      </div>
      <div>
        <div style="font-size:.78rem;font-weight:700;color:#94a3b8;margin-bottom:10px;text-transform:uppercase;letter-spacing:.05em">PASSIVO + PL</div>
        <table class="data-table">
          <tr><td>Fornecedores</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">30.900,00</td></tr>
          <tr><td>Energia a Pagar</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">4.800,00</td></tr>
          <tr><td>Contas a Pagar</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">13.100,00</td></tr>
          <tr><td>Salários a Pagar</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">160.500,00</td></tr>
          <tr><td>IPI a Recolher</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">99.210,00</td></tr>
          <tr><td>ICMS a Recolher</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">216.030,00</td></tr>
          <tr><td>Capital Social</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">2.000.000,00</td></tr>
          <tr><td>Reserva de Lucros</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#34d399">673.327,20</td></tr>
          <tr style="font-weight:700;border-top:2px solid rgba(244,200,66,.3)"><td style="color:#f4c842">TOTAL PASSIVO+PL</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#f4c842">3.197.867,20</td></tr>
        </table>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ==================== TAB: EQUIV PRODUCAO ==================== -->
<div id="tab-equiv" class="tab-content">
<div class="page">
  <div class="section-title">⚖️ Equivalente de Produção</div>

  <div class="card card-gold" style="margin-bottom:20px">
    <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:12px">💡 CONCEITO</div>
    <p style="color:#cbd5e1;font-size:.9rem;line-height:1.7;margin:0">O <strong style="color:#f4c842">Equivalente de Produção</strong> converte unidades em diferentes estágios de conclusão em unidades <em>totalmente acabadas</em> equivalentes. Isso permite calcular um custo unitário único para dividir o CPP.</p>
    <div class="formula-box" style="margin-top:16px">Equiv = Qtd Física × % de Conclusão no Período</div>
  </div>

  <div class="card" style="margin-bottom:20px">
    <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:16px">📊 PREENCHA A TABELA — calcule cada equivalente</div>
    <table class="data-table" id="equivTable">
      <thead>
        <tr>
          <th>Grupo de Unidades</th>
          <th>Qtd Física</th>
          <th>% no Período</th>
          <th style="text-align:center">= Equiv. (preencha)</th>
          <th style="text-align:center">Gabarito</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Est. Elaboração Inicial (completa os 70% restantes)</td>
          <td><span class="highlight">400 und</span></td>
          <td><span class="highlight">70%</span> (100% − 30%)</td>
          <td style="text-align:center"><input class="equiv-input" id="eq1" type="number" placeholder="?"></td>
          <td style="text-align:center;color:#64748b" id="eq1g">—</td>
        </tr>
        <tr>
          <td>Unidades iniciadas e concluídas</td>
          <td><span class="highlight">1.000 und</span></td>
          <td><span class="highlight">100%</span></td>
          <td style="text-align:center"><input class="equiv-input" id="eq2" type="number" placeholder="?"></td>
          <td style="text-align:center;color:#64748b" id="eq2g">—</td>
        </tr>
        <tr>
          <td>Est. Elaboração Final (50% concluído no período)</td>
          <td><span class="highlight">500 und</span></td>
          <td><span class="highlight">50%</span></td>
          <td style="text-align:center"><input class="equiv-input" id="eq3" type="number" placeholder="?"></td>
          <td style="text-align:center;color:#64748b" id="eq3g">—</td>
        </tr>
        <tr style="font-weight:700;background:rgba(244,200,66,.07)">
          <td style="color:#f4c842">TOTAL CPP</td>
          <td colspan="2" style="color:#f4c842">= 280 + 1.000 + 250</td>
          <td style="text-align:center"><input class="equiv-input" id="eq4" type="number" placeholder="Total?" style="border-color:rgba(244,200,66,.5)"></td>
          <td style="text-align:center;color:#64748b" id="eq4g">—</td>
        </tr>
      </tbody>
    </table>
    <div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap">
      <button class="btn btn-gold" onclick="checkEquiv()">✓ Verificar Respostas</button>
      <button class="btn btn-outline" onclick="gabaritoEquiv()">📋 Ver Gabarito</button>
      <button class="btn btn-outline btn-sm" onclick="resetEquiv()">↺ Limpar</button>
    </div>
    <div id="equivMsg"></div>
  </div>

  <div class="card card-green">
    <div style="font-size:.85rem;font-weight:700;color:#34d399;margin-bottom:16px">🔄 FLUXO DE UNIDADES</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px">
      <div class="info-card"><div class="label">Entra (Est. Elab. Inicial)</div><div class="value">400</div><div class="sub">30% concluído</div></div>
      <div class="info-card"><div class="label">+ Iniciadas no Período</div><div class="value">1.000</div><div class="sub">Concluídas 100%</div></div>
      <div class="info-card"><div class="label">= Disponíveis p/ Acabados</div><div class="value">1.400</div><div class="sub">Para o estoque acabados</div></div>
      <div class="info-card"><div class="label">(-) Vendidas</div><div class="value">2.000</div><div class="sub">Total vendas período</div></div>
      <div class="info-card"><div class="label">Est. Elab. Final</div><div class="value">500</div><div class="sub">50% concluído</div></div>
    </div>
    <div style="margin-top:16px;background:#0a0f1e;border-radius:10px;padding:14px;border-left:3px solid #34d399">
      <div style="font-size:.78rem;color:#64748b;margin-bottom:6px">RECONCILIAÇÃO DE UNIDADES</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:.85rem;color:#e2e8f0">
        Est. Acab. Inicial (1.060) + Prod. Acabadas (1.400) = 2.460 disponíveis<br>
        Vendidas (2.000) → Est. Acab. Final = <span style="color:#f4c842;font-weight:700">460 unidades</span>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ==================== TAB: CPP ==================== -->
<div id="tab-cpp" class="tab-content">
<div class="page">
  <div class="section-title">🏭 Custo de Produção do Período (CPP)</div>

  <div class="card card-gold" style="margin-bottom:20px">
    <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:12px">💡 FÓRMULA DO CPP</div>
    <div class="formula-box">CPP = MP + MOD + CIF + Energia (fábrica) + Depreciação Máq. + Depreciação Imóv.</div>
    <p style="color:#cbd5e1;font-size:.85rem;margin:12px 0 0;line-height:1.6">O CPP representa <strong style="color:#f4c842">todos os custos incorridos no processo produtivo</strong> durante o período. Depois de calculado, é dividido pelo total de unidades equivalentes para obter o custo unitário.</p>
  </div>

  <div class="card" style="margin-bottom:20px">
    <div style="font-size:.85rem;font-weight:700;color:#f4c842;margin-bottom:16px">🧮 PREENCHA OS VALORES DO CPP</div>
    <table class="data-table">
      <thead>
        <tr><th>Componente</th><th>Base de Cálculo</th><th style="text-align:right">Valor (preencha)</th><th style="text-align:right">Gabarito</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-blue">MP</span> Matéria Prima</td>
          <td style="font-size:.8rem;color:#94a3b8">1.530 equiv × (1/5 kg) × R$20/kg</td>
          <td style="text-align:right"><input class="cpp-input" id="cpp_mp" type="number" placeholder="R$ ?"></td>
          <td style="text-align:right;color:#64748b" id="cpp_mp_g">—</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">MOD</span> Mão de Obra Direta</td>
          <td style="font-size:.8rem;color:#94a3b8">1.530 equiv × 2h × R$15/h</td>
          <td style="text-align:right"><input class="cpp-input" id="cpp_mod" type="number" placeholder="R$ ?"></td>
          <td style="text-align:right;color:#64748b" id="cpp_mod_g">—</td>
        </tr>
        <tr>
          <td><span class="badge badge-gold">CIF</span> Custos Indiretos</td>
          <td style="font-size:.8rem;color:#94a3b8">Dado do enunciado</td>
          <td style="text-align:right"><input class="cpp-input" id="cpp_cif" type="number" placeholder="R$ ?"></td>
          <td style="text-align:right;color:#64748b" id="cpp_cif_g">—</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">Energia</span> Parcela fábrica (80%)</td>
          <td style="font-size:.8rem;color:#94a3b8">R$1.400 × 80%</td>
          <td style="text-align:right"><input class="cpp-input" id="cpp_en" type="number" placeholder="R$ ?"></td>
          <td style="text-align:right;color:#64748b" id="cpp_en_g">—</td>
        </tr>
        <tr>
          <td><span class="badge badge-red">Dep.</span> Maquinário</td>
          <td style="font-size:.8rem;color:#94a3b8">R$600.000 × 10% ÷ 12 meses</td>
          <td style="text-align:right"><input class="cpp-input" id="cpp_dm" type="number" placeholder="R$ ?"></td>
          <td style="text-align:right;color:#64748b" id="cpp_dm_g">—</td>
        </tr>
        <tr>
          <td><span class="badge badge-red">Dep.</span> Imóveis</td>
          <td style="font-size:.8rem;color:#94a3b8">R$1.200.000 × 4% ÷ 12 meses</td>
          <td style="text-align:right"><input class="cpp-input" id="cpp_di" type="number" placeholder="R$ ?"></td>
          <td style="text-align:right;color:#64748b" id="cpp_di_g">—</td>
        </tr>
        <tr style="font-weight:700;background:rgba(244,200,66,.07);border-top:2px solid rgba(244,200,66,.3)">
          <td style="color:#f4c842">TOTAL CPP</td>
          <td style="font-size:.8rem;color:#f4c842">Soma de todos os componentes</td>
          <td style="text-align:right"><input class="cpp-input" id="cpp_tot" type="number" placeholder="R$ ?" style="border-color:rgba(244,200,66,.5);color:#f4c842"></td>
          <td style="text-align:right;color:#64748b" id="cpp_tot_g">—</td>
        </tr>
      </tbody>
    </table>
    <div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap">
      <button class="btn btn-gold" onclick="checkCPP()">✓ Verificar CPP</button>
      <button class="btn btn-outline" onclick="gabaritoCPP()">📋 Ver Gabarito</button>
      <button class="btn btn-outline btn-sm" onclick="resetCPP()">↺ Limpar</button>
    </div>
    <div id="cppMsg"></div>
  </div>

  <div class="card card-green" id="cppResultCard" style="display:none">
    <div style="font-size:.85rem;font-weight:700;color:#34d399;margin-bottom:16px">📈 CUSTO UNITÁRIO E DISTRIBUIÇÃO</div>
    <div class="info-grid">
      <div class="info-card"><div class="label">CPP Total</div><div class="value">R$ 66.340</div><div class="sub">Total do período</div></div>
      <div class="info-card"><div class="label">÷ Equiv. Produção</div><div class="value">1.530 und</div><div class="sub">Unidades equivalentes</div></div>
      <div class="info-card"><div class="label">= Custo Unitário</div><div class="value">R$ 43,36</div><div class="sub">Por unidade equivalente</div></div>
    </div>
    <hr class="gold">
    <div style="font-size:.78rem;font-weight:700;color:#94a3b8;margin-bottom:12px;text-transform:uppercase">DISTRIBUIÇÃO DO CPP</div>
    <table class="data-table">
      <tr><th>Destino</th><th>Equiv.</th><th>× R$43,36</th><th style="text-align:right">Valor</th></tr>
      <tr><td>Est. Elaboração Final</td><td>250 und</td><td>250 × 43,36</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#f4c842">R$ 10.840,00</td></tr>
      <tr><td>CPA (produtos acabados)</td><td>1.280 und</td><td>1.280 × 43,36</td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#f4c842">R$ 55.500,00</td></tr>
      <tr style="font-weight:700"><td style="color:#f4c842">TOTAL CPP</td><td style="color:#f4c842">1.530 und</td><td></td><td style="text-align:right;font-family:'JetBrains Mono',monospace;color:#f4c842">R$ 66.340,00</td></tr>
    </table>
    <hr class="gold">
    <div style="font-size:.78rem;font-weight:700;color:#94a3b8;margin-bottom:12px;text-transform:uppercase">CPV — MÉTODO MÉDIA PONDERADA</div>
    <table class="data-table">
      <tr><th>Componente</th><th>Qtd</th><th>Valor</th></tr>
      <tr><td>Est. Acabados Inicial</td><td>1.060 und</td><td style="font-family:'JetBrains Mono',monospace">R$ 44.536,00</td></tr>
      <tr><td>+ CPA (prod. acabados no período)</td><td>1.400 und</td><td style="font-family:'JetBrains Mono',monospace">R$ 60.703,20</td></tr>
      <tr><td style="color:#94a3b8;font-size:.8rem">→ CPA = Est. Elab. Inicial + CPP aplicado</td><td style="color:#94a3b8;font-size:.8rem">5.203,20 + 55.500</td><td style="color:#94a3b8;font-size:.8rem;font-family:'JetBrains Mono',monospace">= 60.703,20</td></tr>
      <tr style="border-top:1px solid rgba(244,200,66,.3)"><td>= Total Disponível p/ Venda</td><td>2.460 und</td><td style="font-family:'JetBrains Mono',monospace">R$ 105.239,20</td></tr>
      <tr><td style="color:#f4c842">÷ Custo Médio Ponderado</td><td></td><td style="color:#f4c842;font-family:'JetBrains Mono',monospace;font-weight:700">R$ 42,78/und</td></tr>
      <tr><td>Vendidas × 2.000 und</td><td>2.000 und</td><td style="font-family:'JetBrains Mono',monospace;color:#f4c842;font-weight:700">CPV = R$ 85.560,00</td></tr>
      <tr><td>Est. Acab. Final (460 und × R$42,78)</td><td>460 und</td><td style="font-family:'JetBrains Mono',monospace;color:#34d399">R$ 19.678,80</td></tr>
    </table>
  </div>
  <div style="margin-top:12px"><button class="btn btn-outline" onclick="document.getElementById('cppResultCard').style.display='block'">📊 Ver distribuição e CPV</button></div>
</div>
</div>

<!-- ==================== TAB: RAZONETES ==================== -->
<div id="tab-razonetes" class="tab-content">
<div class="page">
  <div class="section-title">📒 Razonetes (T-Accounts)</div>
  <div class="card" style="margin-bottom:20px">
    <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
      <button class="btn btn-gold" onclick="checkAllRaz()">✓ Verificar Saldos Finais</button>
      <button class="btn btn-outline" onclick="applyGabarito()">📋 Aplicar Gabarito Completo</button>
      <button class="btn btn-outline btn-sm" onclick="resetRazonetes()">↺ Limpar Entradas</button>
      <span style="color:#64748b;font-size:.8rem">| Preencha os saldos finais esperados em cada razonete</span>
    </div>
    <div id="razMsg" style="margin-top:10px"></div>
  </div>
  <div id="razContainer" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px"></div>
</div>
</div>

<!-- ==================== TAB: BALANCO ==================== -->
<div id="tab-balanco" class="tab-content">
<div class="page">
  <div class="section-title">📊 Balanço Patrimonial</div>

  <div style="display:flex;gap:10px;margin-bottom:20px;flex-wrap:wrap">
    <button class="btn btn-gold" onclick="showBP('final')">📊 Balanço Final (após período)</button>
    <button class="btn btn-outline" onclick="showBP('inicial')">📋 Balanço Inicial</button>
    <button class="btn btn-outline" onclick="showBP('ambos')">⚖️ Comparativo</button>
  </div>

  <div id="bpContent"></div>
</div>
</div>

<!-- ==================== TAB: RESOLUCAO ==================== -->
<div id="tab-resolucao" class="tab-content">
<div class="page">
  <div class="section-title">📖 Resolução Passo a Passo</div>

  <div class="card" style="margin-bottom:20px">
    <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
      <button class="btn btn-gold" onclick="startResolucao()" id="btnStartRes">▶ Iniciar</button>
      <button class="btn btn-outline" onclick="prevStep()" id="btnPrev" style="display:none">◀ Anterior</button>
      <button class="btn btn-gold" onclick="nextStep()" id="btnNext" style="display:none">Próximo ▶</button>
      <button class="btn btn-outline btn-sm" onclick="showAllSteps()" id="btnAll" style="display:none">📋 Ver Todos</button>
      <button class="btn btn-outline btn-sm" onclick="resetResolucao()">↺ Reiniciar</button>
      <span id="stepCounter" style="color:#94a3b8;font-size:.85rem;margin-left:10px"></span>
    </div>
    <div id="resProgress" style="display:none;margin-top:12px">
      <div class="progress-bar"><div class="progress-fill" id="resFill" style="width:0%"></div></div>
    </div>
  </div>
  <div id="resContainer"></div>
</div>
</div>

<!-- ==================== TAB: QUIZ ==================== -->
<div id="tab-quiz" class="tab-content">
<div class="page">
  <div class="section-title">🎯 Quiz — Teste seus Conhecimentos</div>
  <div id="quizIntro">
    <div class="card card-gold" style="text-align:center;padding:40px">
      <div style="font-size:3rem;margin-bottom:16px">🎓</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.5rem;color:#f4c842;margin-bottom:12px">Pronto para o Quiz?</div>
      <p style="color:#94a3b8;margin-bottom:24px">12 questões sobre Contabilidade Industrial cobrindo todos os temas deste exercício.</p>
      <button class="btn btn-gold" style="font-size:1rem;padding:14px 36px" onclick="startQuiz()">🚀 Começar Quiz</button>
    </div>
  </div>
  <div id="quizCard" style="display:none">
    <div class="card" style="margin-bottom:16px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">
        <span class="badge badge-gold" id="qBadge">Questão 1 / 12</span>
        <span id="qScore" style="color:#34d399;font-weight:600;font-size:.9rem"></span>
      </div>
      <div class="progress-bar" style="margin-bottom:20px"><div class="progress-fill" id="qFill" style="width:0%"></div></div>
      <div id="qText" style="font-size:1.05rem;color:#e2e8f0;line-height:1.6;margin-bottom:20px"></div>
      <div id="qOptions"></div>
      <div id="qFeedback" style="margin-top:12px"></div>
    </div>
    <div style="display:flex;gap:10px">
      <button class="btn btn-gold" id="btnQNext" onclick="nextQuestion()" style="display:none">Próxima ▶</button>
      <button class="btn btn-outline" id="btnQFinish" onclick="finishQuiz()" style="display:none">Ver Resultado ✓</button>
    </div>
  </div>
  <div id="quizResult" style="display:none">
    <div class="card card-gold" style="text-align:center;padding:40px">
      <div id="resultIcon" style="font-size:3rem;margin-bottom:12px">🏆</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.6rem;color:#f4c842;margin-bottom:8px" id="resultTitle"></div>
      <div style="font-size:1.2rem;color:#e2e8f0;margin-bottom:20px" id="resultScore"></div>
      <div class="progress-bar" style="max-width:300px;margin:0 auto 24px"><div class="progress-fill" id="resultFill"></div></div>
      <div id="reviewList" style="text-align:left;margin-bottom:24px"></div>
      <button class="btn btn-gold" onclick="restartQuiz()">🔄 Tentar Novamente</button>
    </div>
  </div>
</div>
</div>

<script>
// ═══════════════════════════════════════════════
// DATA
// ═══════════════════════════════════════════════
const SI = {
  'BCM':{v:195760,side:'D'},
  'CLIENTES':{v:1184368,side:'D'},
  'ESTOQUE MP':{v:4000,side:'D'},
  'EST. ELABORAÇÃO':{v:5203.20,side:'D'},
  'EST. ACABADOS':{v:44536,side:'D'},
  'MÁQUINAS':{v:600000,side:'D'},
  'IMÓVEIS':{v:1200000,side:'D'},
  'DEP.ACUM.MÁQUINAS':{v:20000,side:'C'},
  'DEP.ACUM.IMÓVEIS':{v:16000,side:'C'},
  'IPI A RECUPERAR':{v:0,side:'D'},
  'ICMS A RECUPERAR':{v:0,side:'D'},
  'FORNECEDORES':{v:30900,side:'C'},
  'ENERGIA A PAGAR':{v:4800,side:'C'},
  'CONTAS A PAGAR':{v:13100,side:'C'},
  'SALÁRIOS A PAGAR':{v:160500,side:'C'},
  'IPI A RECOLHER':{v:99210,side:'C'},
  'ICMS A RECOLHER':{v:216030,side:'C'},
  'CAPITAL SOCIAL':{v:2000000,side:'C'},
  'RESERVA DE LUCROS':{v:673327.20,side:'C'},
  'RECEITA DE VENDAS':{v:0,side:'C'},
  'CPP':{v:0,side:'D'},
  'CPA':{v:0,side:'D'},
  'CPV':{v:0,side:'D'},
  'DESP.ICMS':{v:0,side:'D'},
  'DESP.ENERGIA':{v:0,side:'D'},
  'ARE':{v:0,side:'D'}
};

const LANCAMENTOS = [
  {n:1, desc:"Compra de 500kg de MP a prazo (NF: base R$13.900 + IPI R$1.000)",
   cat:"Compras",
   D:[['ESTOQUE MP',11000],['IPI A RECUPERAR',1000],['ICMS A RECUPERAR',2900]],
   C:[['FORNECEDORES',14900]],
   exp:"Fornecedores = 13.900 + 1.000 (IPI por fora) = R$14.900. O IPI e ICMS são recuperáveis, por isso debitados separadamente. O Estoque MP = 13.900 − 2.900 (ICMS por dentro) = R$11.000."},
  {n:2, desc:"Energia do período (80% fábrica → CPP; 20% escritório → Despesa)",
   cat:"Custos",
   D:[['CPP',1120],['DESP.ENERGIA',280]],
   C:[['ENERGIA A PAGAR',1400]],
   exp:"R$1.400 × 80% = R$1.120 vai ao CPP (custo fabril). R$1.400 × 20% = R$280 é despesa administrativa."},
  {n:3, desc:"Mão de Obra Direta: 1.530 equiv × 2h × R$15/h",
   cat:"Custos",
   D:[['CPP',45900]],
   C:[['SALÁRIOS A PAGAR',45900]],
   exp:"1.530 unidades equivalentes × 2 horas/und × R$15,00/hora = R$45.900."},
  {n:4, desc:"Consumo de Matéria Prima na produção (1.530 equiv ÷ 5 und/kg × R$20/kg)",
   cat:"Custos",
   D:[['CPP',6120]],
   C:[['ESTOQUE MP',6120]],
   exp:"1.530 unidades equiv precisam de 1.530÷5 = 306 kg de MP. 306 kg × R$20,00/kg = R$6.120."},
  {n:5, desc:"Custos Indiretos de Fabricação (CIF) do período",
   cat:"Custos",
   D:[['CPP',4200]],
   C:[['CONTAS A PAGAR',4200]],
   exp:"CIF é dado diretamente no enunciado: R$4.200."},
  {n:6, desc:"Depreciação de Maquinário: R$600.000 × 10% ÷ 12",
   cat:"Custos",
   D:[['CPP',5000]],
   C:[['DEP.ACUM.MÁQUINAS',5000]],
   exp:"R$600.000 × 10% = R$60.000/ano ÷ 12 meses = R$5.000/mês. A depreciação é custo fabril → CPP."},
  {n:7, desc:"Depreciação de Imóveis: R$1.200.000 × 4% ÷ 12",
   cat:"Custos",
   D:[['CPP',4000]],
   C:[['DEP.ACUM.IMÓVEIS',4000]],
   exp:"R$1.200.000 × 4% = R$48.000/ano ÷ 12 meses = R$4.000/mês. CPP total = 6.120+45.900+1.120+4.200+5.000+4.000 = R$66.340."},
  {n:8, desc:"CPP → Est. Elaboração Final (250 equiv × R$43,36)",
   cat:"Apuração",
   D:[['EST. ELABORAÇÃO',10840]],
   C:[['CPP',10840]],
   exp:"Das 1.530 equiv totais, 250 pertencem ao estoque final em elaboração. 250 × R$43,36 = R$10.840. Os outros R$55.500 vão para o CPA."},
  {n:9, desc:"CPP → CPA: custo das unidades concluídas no período",
   cat:"Apuração",
   D:[['CPA',55500]],
   C:[['CPP',55500]],
   exp:"1.280 equiv concluídas × R$43,36 = R$55.500. CPP zerado: 10.840 + 55.500 = 66.340 ✓"},
  {n:10, desc:"Est. Elaboração Inicial → CPA (incorporação do estoque anterior)",
   cat:"Apuração",
   D:[['CPA',5203.20]],
   C:[['EST. ELABORAÇÃO',5203.20]],
   exp:"As 400 und que estavam 30% prontas foram concluídas. Seu custo (R$5.203,20) é transferido ao CPA para compor o custo dos produtos acabados."},
  {n:11, desc:"CPA → Est. Acabados (transferência p/ estoque de produtos acabados)",
   cat:"Apuração",
   D:[['EST. ACABADOS',60703.20]],
   C:[['CPA',60703.20]],
   exp:"CPA = R$55.500 + R$5.203,20 = R$60.703,20. Isso representa o custo de 1.400 unidades físicas transferidas ao estoque de acabados."},
  {n:12, desc:"Venda a prazo: R$570.000 + IPI por fora R$46.000",
   cat:"Vendas",
   D:[['CLIENTES',616000]],
   C:[['RECEITA DE VENDAS',570000],['IPI A RECOLHER',46000]],
   exp:"IPI é 'por fora': o cliente paga R$570.000 (valor base) + R$46.000 (IPI) = R$616.000 total a receber. O IPI é passivo da empresa."},
  {n:13, desc:"ICMS sobre vendas (por dentro — dedução da receita)",
   cat:"Vendas",
   D:[['DESP.ICMS',88000]],
   C:[['ICMS A RECOLHER',88000]],
   exp:"ICMS é 'por dentro': já está embutido no preço de R$570.000. É reconhecido como despesa dedutível da receita e como passivo fiscal."},
  {n:14, desc:"CPV por Média Ponderada: 2.000 und × R$42,78",
   cat:"Vendas",
   D:[['CPV',85560]],
   C:[['EST. ACABADOS',85560]],
   exp:"CMP = (44.536 + 60.703,20) / 2.460 und = R$42,78/und. CPV = 2.000 × R$42,78 = R$85.560. Est. Final = 460 × 42,78 = R$19.678,80."},
  {n:15, desc:"Compensação tributária: IPI a Recuperar vs IPI a Recolher",
   cat:"Tributos",
   D:[['IPI A RECOLHER',1000]],
   C:[['IPI A RECUPERAR',1000]],
   exp:"O IPI pago na compra (R$1.000) compensa parte do IPI a recolher sobre as vendas (R$46.000). Saldo IPI a Recolher = 99.210 + 46.000 − 1.000 = R$144.210."},
  {n:16, desc:"Compensação tributária: ICMS a Recuperar vs ICMS a Recolher",
   cat:"Tributos",
   D:[['ICMS A RECOLHER',2900]],
   C:[['ICMS A RECUPERAR',2900]],
   exp:"O ICMS pago na compra de MP (R$2.900) compensa parte do ICMS sobre vendas. Saldo ICMS = 216.030 + 88.000 − 2.900 = R$301.130."},
  {n:17, desc:"ARE: Encerramento da Receita de Vendas",
   cat:"ARE",
   D:[['RECEITA DE VENDAS',570000]],
   C:[['ARE',570000]],
   exp:"A ARE (Apuração do Resultado do Exercício) recebe todas as contas de resultado. Primeiro, debitamos a Receita para zerá-la e creditamos a ARE."},
  {n:18, desc:"ARE: Encerramento do CPV",
   cat:"ARE",
   D:[['ARE',85560]],
   C:[['CPV',85560]],
   exp:"O CPV é uma conta de custo (débito). Para zerá-la, creditamos CPV e debitamos ARE, transferindo o custo para o resultado."},
  {n:19, desc:"ARE: Encerramento Despesa c/ICMS",
   cat:"ARE",
   D:[['ARE',88000]],
   C:[['DESP.ICMS',88000]],
   exp:"A despesa c/ICMS é transferida para a ARE. Deduz da receita no resultado."},
  {n:20, desc:"ARE: Encerramento Despesa c/Energia (escritório)",
   cat:"ARE",
   D:[['ARE',280]],
   C:[['DESP.ENERGIA',280]],
   exp:"Os 20% de energia do escritório (R$280) são despesa, não custo. Encerrada na ARE."},
  {n:21, desc:"ARE: Lucro Líquido → Reserva de Lucros",
   cat:"ARE",
   D:[['ARE',396160]],
   C:[['RESERVA DE LUCROS',396160]],
   exp:"Lucro = R$570.000 − R$85.560 − R$88.000 − R$280 = R$396.160. A ARE é zerada e o lucro vai para Reserva de Lucros (Patrimônio Líquido)."}
];

// Compute expected final balances
function computeGabarito() {
  const bal = {};
  for (const [acc, data] of Object.entries(SI)) {
    bal[acc] = {D: data.side==='D' ? data.v : 0, C: data.side==='C' ? data.v : 0};
  }
  for (const l of LANCAMENTOS) {
    for (const [acc, v] of l.D) { if (!bal[acc]) bal[acc]={D:0,C:0}; bal[acc].D += v; }
    for (const [acc, v] of l.C) { if (!bal[acc]) bal[acc]={D:0,C:0}; bal[acc].C += v; }
  }
  const result = {};
  for (const [acc, b] of Object.entries(bal)) {
    const si = SI[acc] || {side:'D'};
    const diff = b.D - b.C;
    result[acc] = {saldo: Math.abs(diff), side: diff >= 0 ? 'D' : 'C', D: b.D, C: b.C};
  }
  return result;
}

const GABARITO = computeGabarito();

const fmt = (v) => v.toLocaleString('pt-BR', {minimumFractionDigits:2, maximumFractionDigits:2});

// ═══════════════════════════════════════════════
// TAB NAVIGATION
// ═══════════════════════════════════════════════
function showTab(name) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
  const el = document.getElementById('tab-'+name);
  if (el) el.classList.add('active');
  const btn = document.getElementById('navBtn-'+name);
  if (btn) btn.classList.add('active');
  localStorage.setItem('activeTab', name);
  if (name === 'razonetes') renderRazonetes();
  if (name === 'balanco') showBP('final');
  if (name === 'resolucao') initResolucao();
}

// ═══════════════════════════════════════════════
// EQUIV PRODUÇÃO
// ═══════════════════════════════════════════════
const eqAnswers = [280, 1000, 250, 1530];
function checkEquiv() {
  const ids = ['eq1','eq2','eq3','eq4'];
  let correct = 0;
  ids.forEach((id, i) => {
    const val = parseFloat(document.getElementById(id).value);
    const el = document.getElementById(id);
    if (val === eqAnswers[i]) { el.style.borderColor='#10b981'; correct++; document.getElementById(id+'g').textContent = '✓ '+eqAnswers[i]; document.getElementById(id+'g').style.color='#34d399'; }
    else { el.style.borderColor='#ef4444'; }
  });
  const msg = document.getElementById('equivMsg');
  msg.innerHTML = correct===4
    ? '<div class="msg msg-success">✅ Perfeito! Todos os equivalentes estão corretos. Total CPP = 1.530 und.</div>'
    : '<div class="msg msg-error">❌ '+correct+'/4 corretos. Revise: Equiv = Qtd Física × % no período atual.</div>';
}
function gabarito() { document.getElementById('equivMsg').innerHTML=''; }
function gabaritEquiv() {}
function gabaritoEquiv() {
  const ids = ['eq1','eq2','eq3','eq4'];
  ids.forEach((id,i) => {
    document.getElementById(id).value = eqAnswers[i];
    document.getElementById(id).style.borderColor='rgba(244,200,66,.5)';
    document.getElementById(id+'g').textContent = eqAnswers[i];
    document.getElementById(id+'g').style.color='#f4c842';
  });
  document.getElementById('equivMsg').innerHTML='<div class="msg msg-info">📋 Gabarito aplicado.</div>';
}
function resetEquiv() {
  ['eq1','eq2','eq3','eq4'].forEach(id => {
    document.getElementById(id).value='';
    document.getElementById(id).style.borderColor='#243558';
    document.getElementById(id+'g').textContent='—';
    document.getElementById(id+'g').style.color='#64748b';
  });
  document.getElementById('equivMsg').innerHTML='';
}

// ═══════════════════════════════════════════════
// CPP
// ═══════════════════════════════════════════════
const cppAnswers = {cpp_mp:6120,cpp_mod:45900,cpp_cif:4200,cpp_en:1120,cpp_dm:5000,cpp_di:4000,cpp_tot:66340};
function checkCPP() {
  let correct=0, total=Object.keys(cppAnswers).length;
  for (const [id, ans] of Object.entries(cppAnswers)) {
    const val = parseFloat(document.getElementById(id).value);
    const el = document.getElementById(id);
    const gel = document.getElementById(id+'_g');
    if (val === ans) { el.style.borderColor='#10b981'; correct++; gel.textContent='✓ R$ '+fmt(ans); gel.style.color='#34d399'; }
    else { el.style.borderColor='#ef4444'; gel.textContent='R$ '+fmt(ans); gel.style.color='#fca5a5'; }
  }
  const msg = document.getElementById('cppMsg');
  msg.innerHTML = correct===total
    ? '<div class="msg msg-success">✅ CPP correto! Total = R$ 66.340,00</div>'
    : '<div class="msg msg-error">❌ '+correct+'/'+total+' corretos.</div>';
}
function gabaritoCPP() {
  for (const [id, ans] of Object.entries(cppAnswers)) {
    document.getElementById(id).value = ans;
    document.getElementById(id).style.borderColor='rgba(244,200,66,.5)';
    document.getElementById(id+'_g').textContent='R$ '+fmt(ans);
    document.getElementById(id+'_g').style.color='#f4c842';
  }
  document.getElementById('cppMsg').innerHTML='<div class="msg msg-info">📋 Gabarito aplicado.</div>';
}
function resetCPP() {
  for (const id of Object.keys(cppAnswers)) {
    document.getElementById(id).value='';
    document.getElementById(id).style.borderColor='#243558';
    document.getElementById(id+'_g').textContent='—';
    document.getElementById(id+'_g').style.color='#64748b';
  }
  document.getElementById('cppMsg').innerHTML='';
}

// ═══════════════════════════════════════════════
// RAZONETES
// ═══════════════════════════════════════════════
const RAZ_ACCOUNTS = Object.keys(SI);
const catColors = {D:'#93c5fd',C:'#fca5a5'};

function buildRazTransactions(acc) {
  const entries = [];
  for (const l of LANCAMENTOS) {
    for (const [a, v] of l.D) { if (a===acc) entries.push({n:l.n, side:'D', v}); }
    for (const [a, v] of l.C) { if (a===acc) entries.push({n:l.n, side:'C', v}); }
  }
  return entries;
}

function renderRazonetes() {
  const container = document.getElementById('razContainer');
  if (!container || container.dataset.rendered) return;
  container.dataset.rendered = '1';
  let html = '';
  for (const acc of RAZ_ACCOUNTS) {
    const si = SI[acc];
    const txs = buildRazTransactions(acc);
    const g = GABARITO[acc];
    const savedD = localStorage.getItem('raz_D_'+acc) || '';
    const savedC = localStorage.getItem('raz_C_'+acc) || '';

    html += '<div class="razonete" id="raz-'+acc.replace(/[^a-z0-9]/gi,'_')+'">';
    html += '<div class="raz-name">'+acc+'</div>';
    html += '<div class="raz-grid">';
    html += '<div class="raz-col-header raz-debit">DÉBITO</div>';
    html += '<div class="raz-col-header">CRÉDITO</div>';

    // SI row
    if (si.side==='D' && si.v>0) {
      html += '<div class="raz-entry si"><span><span class="ref">SI</span><span class="val">'+fmt(si.v)+'</span></span><span></span></div>';
      html += '<div class="raz-entry si" style="border-left:1px solid #243558"><span></span></div>';
    } else if (si.side==='C' && si.v>0) {
      html += '<div class="raz-entry si"><span></span></div>';
      html += '<div class="raz-entry si" style="border-left:1px solid #243558"><span><span class="ref">SI</span><span class="val">'+fmt(si.v)+'</span></span></div>';
    }

    // Transaction rows
    const debits = txs.filter(t=>t.side==='D');
    const credits = txs.filter(t=>t.side==='C');
    const maxRows = Math.max(debits.length, credits.length);
    for (let i=0; i<maxRows; i++) {
      const d = debits[i], c = credits[i];
      html += '<div class="raz-entry" style="border-right:1px solid #243558">';
      if (d) html += '<span class="ref">('+d.n+')</span><span class="val" style="color:#93c5fd">'+fmt(d.v)+'</span>';
      html += '</div>';
      html += '<div class="raz-entry">';
      if (c) html += '<span class="ref">('+c.n+')</span><span class="val" style="color:#fca5a5">'+fmt(c.v)+'</span>';
      html += '</div>';
    }

    // Saldo input row
    const sideLbl = g.side==='D' ? 'Sd (D)' : 'Sc (C)';
    html += '<div class="raz-entry saldo" style="border-right:1px solid #243558">';
    html += g.side==='D' ? '<span style="font-size:.7rem;color:#64748b">'+sideLbl+'</span><input type="number" class="equiv-input" style="width:100px" placeholder="Saldo?" id="razIn_D_'+acc.replace(/[^a-z0-9]/gi,'_')+'" value="'+savedD+'" onchange="saveRaz(\''+acc.replace(/'/g,"\\'")+'\')">' : '<span></span>';
    html += '</div>';
    html += '<div class="raz-entry saldo">';
    html += g.side==='C' ? '<span style="font-size:.7rem;color:#64748b">'+sideLbl+'</span><input type="number" class="equiv-input" style="width:100px" placeholder="Saldo?" id="razIn_C_'+acc.replace(/[^a-z0-9]/gi,'_')+'" value="'+savedC+'" onchange="saveRaz(\''+acc.replace(/'/g,"\\'")+'\')">' : '<span></span>';
    html += '</div>';

    html += '</div></div>'; // raz-grid + razonete
  }
  container.innerHTML = html;
}

function saveRaz(acc) {
  const key = acc.replace(/[^a-z0-9]/gi,'_');
  const dEl = document.getElementById('razIn_D_'+key);
  const cEl = document.getElementById('razIn_C_'+key);
  if (dEl) localStorage.setItem('raz_D_'+acc, dEl.value);
  if (cEl) localStorage.setItem('raz_C_'+acc, cEl.value);
}

function checkAllRaz() {
  let correct=0, total=0;
  for (const acc of RAZ_ACCOUNTS) {
    const g = GABARITO[acc];
    const key = acc.replace(/[^a-z0-9]/gi,'_');
    const inputId = 'razIn_'+g.side+'_'+key;
    const el = document.getElementById(inputId);
    if (!el) continue;
    total++;
    const val = parseFloat(el.value);
    if (Math.abs(val - g.saldo) < 0.05) {
      correct++;
      el.style.borderColor='#10b981';
    } else {
      el.style.borderColor='#ef4444';
    }
  }
  document.getElementById('razMsg').innerHTML = correct===total
    ? '<div class="msg msg-success">✅ Todos os saldos corretos! Balanço equilibrado.</div>'
    : '<div class="msg msg-error">❌ '+correct+'/'+total+' saldos corretos. Os campos em vermelho precisam de revisão.</div>';
}

function applyGabarito() {
  for (const acc of RAZ_ACCOUNTS) {
    const g = GABARITO[acc];
    const key = acc.replace(/[^a-z0-9]/gi,'_');
    const dEl = document.getElementById('razIn_D_'+key);
    const cEl = document.getElementById('razIn_C_'+key);
    if (dEl) { dEl.value = g.side==='D' ? g.saldo.toFixed(2) : ''; dEl.style.borderColor='rgba(244,200,66,.5)'; }
    if (cEl) { cEl.value = g.side==='C' ? g.saldo.toFixed(2) : ''; cEl.style.borderColor='rgba(244,200,66,.5)'; }
  }
  document.getElementById('razMsg').innerHTML='<div class="msg msg-info">📋 Gabarito aplicado a todos os razonetes.</div>';
}

function resetRazonetes() {
  for (const acc of RAZ_ACCOUNTS) {
    const key = acc.replace(/[^a-z0-9]/gi,'_');
    ['D','C'].forEach(s => {
      const el = document.getElementById('razIn_'+s+'_'+key);
      if (el) { el.value=''; el.style.borderColor='#243558'; }
    });
    localStorage.removeItem('raz_D_'+acc);
    localStorage.removeItem('raz_C_'+acc);
  }
  document.getElementById('razMsg').innerHTML='';
}

// ═══════════════════════════════════════════════
// BALANÇO PATRIMONIAL
// ═══════════════════════════════════════════════
const BP_ATIVO_I = [
  {label:'ATIVO CIRCULANTE', header:true},
  {acc:'BCM', label:'Banco Conta Movimento'},
  {acc:'CLIENTES', label:'Clientes'},
  {acc:'ESTOQUE MP', label:'Estoque de Matéria Prima'},
  {acc:'EST. ELABORAÇÃO', label:'Est. Prod. em Elaboração'},
  {acc:'EST. ACABADOS', label:'Est. Prod. Acabados'},
  {label:'ATIVO NÃO CIRCULANTE', header:true},
  {acc:'MÁQUINAS', label:'Máquinas'},
  {acc:'DEP.ACUM.MÁQUINAS', label:'(−) Dep. Acum. Máquinas', neg:true},
  {acc:'IMÓVEIS', label:'Imóveis'},
  {acc:'DEP.ACUM.IMÓVEIS', label:'(−) Dep. Acum. Imóveis', neg:true},
];
const BP_PASSIVO_I = [
  {label:'PASSIVO CIRCULANTE', header:true},
  {acc:'FORNECEDORES', label:'Fornecedores'},
  {acc:'ENERGIA A PAGAR', label:'Energia a Pagar'},
  {acc:'CONTAS A PAGAR', label:'Contas a Pagar'},
  {acc:'SALÁRIOS A PAGAR', label:'Salários a Pagar'},
  {acc:'IPI A RECOLHER', label:'IPI a Recolher'},
  {acc:'ICMS A RECOLHER', label:'ICMS a Recolher'},
  {label:'PATRIMÔNIO LÍQUIDO', header:true},
  {acc:'CAPITAL SOCIAL', label:'Capital Social'},
  {acc:'RESERVA DE LUCROS', label:'Reserva de Lucros'},
];

function bpVal(acc, useGabarito) {
  if (!acc) return 0;
  if (useGabarito) return GABARITO[acc] ? GABARITO[acc].saldo : 0;
  return SI[acc] ? SI[acc].v : 0;
}

function renderBPTable(items, useGabarito, label) {
  let html = '<div class="bp-section">';
  let total = 0;
  for (const row of items) {
    if (row.header) {
      html += '<div class="bp-row header"><span>'+row.label+'</span></div>';
    } else {
      const v = bpVal(row.acc, useGabarito);
      const sign = row.neg ? -v : v;
      total += sign;
      html += '<div class="bp-row"><span>'+row.label+'</span><span style="font-family:\'JetBrains Mono\',monospace;color:'+(row.neg?'#fca5a5':'#e2e8f0')+'">R$ '+(row.neg?'('+fmt(v)+')':fmt(v))+'</span></div>';
    }
  }
  html += '<div class="bp-row total"><span>TOTAL '+label+'</span><span style="font-family:\'JetBrains Mono\',monospace">R$ '+fmt(total)+'</span></div>';
  html += '</div>';
  return {html, total};
}

function showBP(mode) {
  const cont = document.getElementById('bpContent');
  if (!cont) return;
  if (mode==='inicial') {
    const a = renderBPTable(BP_ATIVO_I, false, 'ATIVO');
    const p = renderBPTable(BP_PASSIVO_I, false, 'PASSIVO + PL');
    cont.innerHTML = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px"><div class="card"><div style="font-family:\'Playfair Display\',serif;color:#f4c842;font-size:1.1rem;margin-bottom:16px">ATIVO — Inicial</div>'+a.html+'</div><div class="card"><div style="font-family:\'Playfair Display\',serif;color:#f4c842;font-size:1.1rem;margin-bottom:16px">PASSIVO + PL — Inicial</div>'+p.html+'</div></div>';
  } else if (mode==='final') {
    const a = renderBPTable(BP_ATIVO_I, true, 'ATIVO');
    const p = renderBPTable(BP_PASSIVO_I, true, 'PASSIVO + PL');
    const eq = Math.abs(a.total - p.total) < 1;
    cont.innerHTML = '<div class="msg '+(eq?'msg-success':'msg-error')+'" style="margin-bottom:16px">'+(eq?'✅ Balanço equilibrado! Ativo = Passivo + PL':'⚠️ Diferença de R$ '+fmt(Math.abs(a.total-p.total)))+'</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:20px"><div class="card"><div style="font-family:\'Playfair Display\',serif;color:#f4c842;font-size:1.1rem;margin-bottom:16px">ATIVO — Final</div>'+a.html+'</div><div class="card"><div style="font-family:\'Playfair Display\',serif;color:#f4c842;font-size:1.1rem;margin-bottom:16px">PASSIVO + PL — Final</div>'+p.html+'</div></div>';
  } else {
    const ai = renderBPTable(BP_ATIVO_I, false, 'ATIVO INICIAL');
    const af = renderBPTable(BP_ATIVO_I, true, 'ATIVO FINAL');
    const pi = renderBPTable(BP_PASSIVO_I, false, 'PASSIVO+PL INICIAL');
    const pf = renderBPTable(BP_PASSIVO_I, true, 'PASSIVO+PL FINAL');
    cont.innerHTML = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px"><div class="card"><div style="font-family:\'Playfair Display\',serif;color:#f4c842;font-size:1.1rem;margin-bottom:16px">ATIVO Inicial vs Final</div>'+ai.html+'<hr class="gold">'+af.html+'</div><div class="card"><div style="font-family:\'Playfair Display\',serif;color:#f4c842;font-size:1.1rem;margin-bottom:16px">PASSIVO+PL Inicial vs Final</div>'+pi.html+'<hr class="gold">'+pf.html+'</div></div>';
  }
}

// ═══════════════════════════════════════════════
// RESOLUÇÃO
// ═══════════════════════════════════════════════
let currentStep = -1;
let allVisible = false;

function initResolucao() {
  if (currentStep === -1) {
    document.getElementById('resContainer').innerHTML = '<div class="card card-gold" style="text-align:center;padding:30px"><div style="font-size:2rem;margin-bottom:12px">📖</div><p style="color:#94a3b8">Clique em <strong style="color:#f4c842">Iniciar</strong> para ver os lançamentos passo a passo, ou use <strong style="color:#f4c842">Ver Todos</strong> para exibir todos de uma vez.</p></div>';
  }
}

function startResolucao() {
  currentStep = 0;
  allVisible = false;
  document.getElementById('btnStartRes').style.display='none';
  document.getElementById('btnPrev').style.display='inline-block';
  document.getElementById('btnNext').style.display='inline-block';
  document.getElementById('btnAll').style.display='inline-block';
  document.getElementById('resProgress').style.display='block';
  renderCurrentStep();
}

function renderCurrentStep() {
  const l = LANCAMENTOS[currentStep];
  document.getElementById('stepCounter').textContent = 'Lançamento '+(currentStep+1)+' de '+LANCAMENTOS.length;
  document.getElementById('resFill').style.width = ((currentStep+1)/LANCAMENTOS.length*100)+'%';

  const catCol = {Compras:'#60a5fa',Custos:'#34d399',Apuração:'#f4c842',Vendas:'#a78bfa',Tributos:'#fb923c',ARE:'#f87171'};
  const col = catCol[l.cat] || '#94a3b8';

  let debitRows = l.D.map(([a,v]) => `<div class="je-line"><span></span><span class="acct-debit">${a}</span><span class="val-debit">R$ ${fmt(v)}</span><span></span></div>`).join('');
  let creditRows = l.C.map(([a,v]) => `<div class="je-line"><span></span><span class="acct-credit">${a}</span><span></span><span class="val-credit">R$ ${fmt(v)}</span></div>`).join('');

  document.getElementById('resContainer').innerHTML = `
    <div class="step-card active-step">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
        <div style="background:${col};color:#0a0f1e;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">${l.n}</div>
        <div>
          <div style="font-size:.75rem;color:${col};font-weight:700;text-transform:uppercase;letter-spacing:.05em">${l.cat}</div>
          <div style="font-size:.92rem;color:#e2e8f0">${l.desc}</div>
        </div>
      </div>
      <div style="background:#0a0f1e;border-radius:10px;padding:16px;margin-bottom:14px">
        <div style="display:grid;grid-template-columns:40px 220px 1fr 1fr;gap:8px;padding:4px 0;margin-bottom:6px;border-bottom:1px solid #243558">
          <span style="font-size:.7rem;color:#64748b">#</span>
          <span style="font-size:.7rem;color:#64748b;text-transform:uppercase">Conta</span>
          <span style="font-size:.7rem;color:#64748b;text-align:right;text-transform:uppercase">Débito</span>
          <span style="font-size:.7rem;color:#64748b;text-align:right;text-transform:uppercase">Crédito</span>
        </div>
        ${debitRows}${creditRows}
      </div>
      <div style="background:rgba(96,165,250,.06);border:1px solid rgba(96,165,250,.2);border-radius:8px;padding:12px;font-size:.85rem;color:#cbd5e1;line-height:1.6">
        💡 <strong style="color:#93c5fd">Explicação:</strong> ${l.exp}
      </div>
    </div>
  `;
}

function nextStep() {
  if (currentStep < LANCAMENTOS.length-1) { currentStep++; renderCurrentStep(); }
  else { document.getElementById('resContainer').innerHTML += '<div class="msg msg-success" style="margin-top:16px">✅ Todos os lançamentos concluídos! Total: 21 lançamentos registrados.</div>'; }
}

function prevStep() {
  if (currentStep > 0) { currentStep--; renderCurrentStep(); }
}

function showAllSteps() {
  document.getElementById('resProgress').style.display='none';
  document.getElementById('btnPrev').style.display='none';
  document.getElementById('btnNext').style.display='none';
  document.getElementById('btnAll').style.display='none';
  document.getElementById('stepCounter').textContent='';

  const catCol = {Compras:'#60a5fa',Custos:'#34d399',Apuração:'#f4c842',Vendas:'#a78bfa',Tributos:'#fb923c',ARE:'#f87171'};
  let html = '';
  for (const l of LANCAMENTOS) {
    const col = catCol[l.cat] || '#94a3b8';
    let debitRows = l.D.map(([a,v]) => `<div class="je-line"><span></span><span class="acct-debit">${a}</span><span class="val-debit">R$ ${fmt(v)}</span><span></span></div>`).join('');
    let creditRows = l.C.map(([a,v]) => `<div class="je-line"><span></span><span class="acct-credit">${a}</span><span></span><span class="val-credit">R$ ${fmt(v)}</span></div>`).join('');
    html += `<div class="step-card" style="margin-bottom:10px">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
        <div style="background:${col};color:#0a0f1e;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.8rem;flex-shrink:0">${l.n}</div>
        <span style="font-size:.85rem;color:#e2e8f0">${l.desc}</span>
        <span class="badge" style="background:rgba(0,0,0,.3);color:${col};border-color:${col};margin-left:auto;white-space:nowrap">${l.cat}</span>
      </div>
      <div style="background:#0a0f1e;border-radius:8px;padding:12px;font-size:.82rem">${debitRows}${creditRows}</div>
    </div>`;
  }
  document.getElementById('resContainer').innerHTML = html;
}

function resetResolucao() {
  currentStep = -1;
  allVisible = false;
  document.getElementById('btnStartRes').style.display='inline-block';
  document.getElementById('btnPrev').style.display='none';
  document.getElementById('btnNext').style.display='none';
  document.getElementById('btnAll').style.display='none';
  document.getElementById('resProgress').style.display='none';
  document.getElementById('stepCounter').textContent='';
  initResolucao();
}

// ═══════════════════════════════════════════════
// QUIZ
// ═══════════════════════════════════════════════
const QUIZ = [
  {q:"Qual é o total do Equivalente de Produção (CPP) neste exercício?",
   opts:["1.280 unidades","1.400 unidades","1.530 unidades","1.750 unidades"],
   ans:2,
   exp:"280 (WIP inicial completa 70%) + 1.000 (novas concluídas) + 250 (WIP final 50%) = 1.530 unidades equivalentes."},
  {q:"Qual é o CPP total do período?",
   opts:["R$ 56.220,00","R$ 61.340,00","R$ 66.340,00","R$ 70.500,00"],
   ans:2,
   exp:"CPP = MP (6.120) + MOD (45.900) + CIF (4.200) + Energia fábrica (1.120) + Dep.Máq (5.000) + Dep.Imóv (4.000) = R$66.340."},
  {q:"O custo unitário de produção (CPP/equiv) é:",
   opts:["R$ 40,00","R$ 42,78","R$ 43,36","R$ 45,00"],
   ans:2,
   exp:"R$66.340 ÷ 1.530 equiv = R$43,36 por unidade equivalente."},
  {q:"O CPV foi calculado pelo método da Média Ponderada. Qual o custo unitário médio?",
   opts:["R$ 41,99","R$ 42,78","R$ 43,36","R$ 44,53"],
   ans:1,
   exp:"(Est.Acab.Inicial R$44.536 + CPA R$60.703,20) ÷ 2.460 und disponíveis = R$42,78/und."},
  {q:"O IPI sobre a compra de MP (R$1.000) é contabilizado como:",
   opts:["Custo do estoque de MP","Despesa imediata","IPI a Recuperar (ativo)","Passivo fiscal"],
   ans:2,
   exp:"O IPI nas compras é recuperável (não-cumulativo). É debitado em 'IPI a Recuperar' e posteriormente compensado com o IPI sobre vendas."},
  {q:"O ICMS de R$2.900 na compra de MP: que efeito tem no custo do estoque?",
   opts:["Aumenta o custo do estoque em R$2.900","Não afeta o custo do estoque (fica em recuperar)","É lançado a resultado imediatamente","Aumenta a conta Fornecedores em R$2.900"],
   ans:1,
   exp:"O ICMS nas compras é recuperável. O estoque de MP é registrado por R$11.000 (13.900 − 2.900), sem incluir o ICMS que vai para 'ICMS a Recuperar'."},
  {q:"A energia do escritório (20% = R$280) é classificada como:",
   opts:["Custo de produção → CPP","Custo indireto de fabricação (CIF)","Despesa do período → ARE","Ativo diferido"],
   ans:2,
   exp:"Apenas os 80% de energia fabril vão ao CPP. Os 20% do escritório são despesa administrativa, encerrada na ARE."},
  {q:"Quantas unidades físicas foram transferidas para o Est. Acabados no período?",
   opts:["1.000 unidades","1.280 unidades","1.400 unidades","1.530 unidades"],
   ans:2,
   exp:"400 und do Est.Elab inicial (completadas) + 1.000 und novas (concluídas 100%) = 1.400 unidades físicas acabadas."},
  {q:"O total de clientes a receber após as vendas é:",
   opts:["R$ 570.000","R$ 616.000","R$ 524.000","R$ 658.000"],
   ans:1,
   exp:"Clientes = R$570.000 (base) + R$46.000 (IPI por fora) = R$616.000. O IPI é cobrado 'por fora' do preço de venda."},
  {q:"O lucro líquido do período (ARE) é:",
   opts:["R$ 310.440","R$ 396.160","R$ 481.440","R$ 485.720"],
   ans:1,
   exp:"Lucro = R$570.000 (receita) − R$85.560 (CPV) − R$88.000 (ICMS) − R$280 (energia escritório) = R$396.160."},
  {q:"A depreciação de imóveis (R$1.200.000 × 4% a.a.) por mês é:",
   opts:["R$ 5.000","R$ 6.000","R$ 4.000","R$ 3.600"],
   ans:2,
   exp:"R$1.200.000 × 4% = R$48.000/ano ÷ 12 meses = R$4.000/mês. Nota: R$6.000 seria para imóveis de R$1.800.000 (exercício anterior)."},
  {q:"O Est. Prod. Acabados ao final do período contém:",
   opts:["400 unidades","460 unidades","500 unidades","560 unidades"],
   ans:1,
   exp:"1.060 (inicial) + 1.400 (produzidas e acabadas) − 2.000 (vendidas) = 460 unidades em estoque final."},
];

let qIndex = 0, qScore = 0, qAnswered = [];

function startQuiz() {
  qIndex=0; qScore=0; qAnswered=[];
  document.getElementById('quizIntro').style.display='none';
  document.getElementById('quizResult').style.display='none';
  document.getElementById('quizCard').style.display='block';
  renderQuestion();
}

function renderQuestion() {
  const q = QUIZ[qIndex];
  document.getElementById('qBadge').textContent='Questão '+(qIndex+1)+' / '+QUIZ.length;
  document.getElementById('qScore').textContent='Acertos: '+qScore;
  document.getElementById('qFill').style.width=((qIndex)/QUIZ.length*100)+'%';
  document.getElementById('qText').textContent=q.q;
  document.getElementById('qFeedback').innerHTML='';
  document.getElementById('btnQNext').style.display='none';
  document.getElementById('btnQFinish').style.display='none';

  let html='';
  q.opts.forEach((opt,i) => {
    html+=`<button class="quiz-option" onclick="selectOption(${i})" id="qopt${i}">${String.fromCharCode(65+i)}) ${opt}</button>`;
  });
  document.getElementById('qOptions').innerHTML=html;
}

function selectOption(i) {
  const q = QUIZ[qIndex];
  document.querySelectorAll('.quiz-option').forEach(b => b.disabled=true);
  document.getElementById('qopt'+i).classList.add('selected');

  if (i===q.ans) {
    qScore++;
    document.getElementById('qopt'+i).classList.add('correct');
    document.getElementById('qFeedback').innerHTML='<div class="msg msg-success">✅ Correto! '+q.exp+'</div>';
  } else {
    document.getElementById('qopt'+i).classList.add('wrong');
    document.getElementById('qopt'+q.ans).classList.add('correct');
    document.getElementById('qFeedback').innerHTML='<div class="msg msg-error">❌ Incorreto. '+q.exp+'</div>';
  }
  qAnswered.push({q:q.q, chosen:i, correct:q.ans, ok:i===q.ans});

  if (qIndex < QUIZ.length-1) document.getElementById('btnQNext').style.display='inline-block';
  else document.getElementById('btnQFinish').style.display='inline-block';
}

function nextQuestion() {
  qIndex++;
  document.getElementById('btnQNext').style.display='none';
  renderQuestion();
}

function finishQuiz() {
  document.getElementById('quizCard').style.display='none';
  document.getElementById('quizResult').style.display='block';
  const pct = Math.round(qScore/QUIZ.length*100);
  const icon = pct>=90?'🏆':pct>=70?'🎓':pct>=50?'📚':'💪';
  const title = pct>=90?'Excelente!':pct>=70?'Muito Bom!':pct>=50?'Continue Estudando':'Precisa Revisar';
  document.getElementById('resultIcon').textContent=icon;
  document.getElementById('resultTitle').textContent=title;
  document.getElementById('resultScore').textContent=qScore+' de '+QUIZ.length+' corretas ('+pct+'%)';
  document.getElementById('resultFill').style.width=pct+'%';

  let reviewHtml='<div style="font-size:.8rem;font-weight:700;color:#94a3b8;margin-bottom:10px;text-transform:uppercase">REVISÃO</div>';
  qAnswered.forEach((a,i) => {
    reviewHtml += '<div style="display:flex;gap:8px;padding:8px;border-radius:6px;margin-bottom:6px;background:'+(a.ok?'rgba(16,185,129,.07)':'rgba(239,68,68,.07')+';border:1px solid '+(a.ok?'rgba(16,185,129,.2)':'rgba(239,68,68,.2)')+'"><span>'+(a.ok?'✅':'❌')+'</span><span style="font-size:.82rem;color:#e2e8f0">'+a.q+'</span></div>';
  });
  document.getElementById('reviewList').innerHTML=reviewHtml;
}

function restartQuiz() {
  document.getElementById('quizResult').style.display='none';
  startQuiz();
}

// ═══════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('activeTab') || 'enunciado';
  showTab(saved);
});
</script>
</body>
</html>"""

with open('/sessions/bold-jolly-hamilton/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("File written successfully. Size:", len(html), "chars")
