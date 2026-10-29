"use client";
import {useEffect,useState,type CSSProperties} from "react";
type Test={name:string;passed:boolean;error?:string|null;input?:string;expected?:string;actual?:string;expected_output?:string;actual_output?:string;hidden?:boolean};
type Result={status:string;passed:number;total:number;score:number;execution_time_ms:number;tests?:Test[];stdout?:string;stderr?:string;error?:string|null};
type Example={input:string;output:string;explanation?:string};
type PublicCase={name:string;input?:string|null;expected?:string|null};
type Props={questionId:string;visibleTests?:(string|PublicCase)[];examples?:Example[];result:Result|null;action?:'run'|'submit'|null;running?:boolean;error?:string;publicTestCount?:number};
const mono:CSSProperties={margin:'7px 0 16px',padding:'13px 14px',borderRadius:7,background:'#f3f4f6',color:'#202124',fontFamily:'Consolas,monospace',fontSize:13,whiteSpace:'pre-wrap',overflowWrap:'anywhere',lineHeight:1.7};
const muted:CSSProperties={color:'#737373',fontSize:12,fontWeight:600,marginTop:14,marginBottom:4};
export default function JudgePanel({questionId,visibleTests=[],examples=[],result,action,running=false,error='',publicTestCount=2}:Props){
 const [tab,setTab]=useState<'testcase'|'result'>('testcase');const [selected,setSelected]=useState(0);
 useEffect(()=>{setTab('testcase');setSelected(0)},[questionId]);useEffect(()=>{if(result||error||running){setTab('result');setSelected(0)}},[result,error,running]);
 const tests=result?.tests||[];const submission=action==='submit';const hidden=(t:Test,i:number)=>t.hidden===true||/hidden|private/i.test(t.name)||(submission&&i>=publicTestCount);const chosen=tests[selected],privateCase=chosen?hidden(chosen,selected):false;
 const testCount=tab==='testcase'?Math.max(visibleTests.length,examples.length):tests.length;const accepted=result?.status==='passed';
 return <section style={{border:'1px solid #e0e0e0',background:'white',borderRadius:10,overflow:'hidden',marginTop:12}}>
  <nav style={{height:45,display:'flex',alignItems:'stretch',gap:20,padding:'0 18px',borderBottom:'1px solid #eee'}}>{(['testcase','result'] as const).map(t=><button key={t} type="button" onClick={()=>{setTab(t);setSelected(0)}} style={{background:'transparent',border:0,borderBottom:tab===t?'2px solid #222':'2px solid transparent',fontWeight:700,fontSize:13,color:tab===t?'#262626':'#888',cursor:'pointer'}}>{t==='testcase'?'▣ Testcase':'◉ Test Result'}</button>)}</nav>
  <div style={{padding:18,minHeight:180}}>
  {tab==='testcase'?<>
   {testCount?<div style={{display:'flex',gap:8,flexWrap:'wrap'}}>{Array.from({length:testCount},(_,i)=><button key={i} onClick={()=>setSelected(i)} style={{padding:'9px 13px',border:0,borderRadius:7,background:selected===i?'#e9e9e9':'#f5f5f5',color:'#303030',fontWeight:650,cursor:'pointer'}}>Case {i+1}</button>)}</div>:<p style={{fontSize:13,color:'#888'}}>No public sample cases provided for this question.</p>}
   {testCount>0&&<><div style={muted}>Input</div><pre style={mono}>{typeof visibleTests[selected]==='object' && visibleTests[selected]!==null ? ((visibleTests[selected] as PublicCase).input ?? 'Input not yet configured') : (examples[selected]?.input ?? 'Input not available')}</pre><div style={muted}>Expected Output (example)</div><pre style={mono}>{typeof visibleTests[selected]==='object' && visibleTests[selected]!==null ? ((visibleTests[selected] as PublicCase).expected ?? 'Expected output not yet configured') : (examples[selected]?.output ?? 'Expected output not available')}</pre>{examples[selected]?.explanation&&<p style={{fontSize:12,color:'#777'}}>{examples[selected].explanation}</p>}</>}
   <div style={{color:'#777',fontSize:12,marginTop:12}}>Verified public test cases are shown above. Private test inputs and expected outputs are never disclosed.</div>
  </>:<>
   {running&&<div style={{fontSize:14,color:'#666'}}>Evaluating test cases...</div>}
   {!running&&!result&&!error&&<p style={{fontSize:13,color:'#777'}}>Run Code checks sample tests. Submit Code checks the complete configured suite.</p>}
   {error&&<pre style={{...mono,color:'#b42318'}}>{error}</pre>}
   {result&&<><div style={{display:'flex',justifyContent:'space-between',gap:12,alignItems:'center',flexWrap:'wrap',marginBottom:14}}><div><strong style={{fontSize:21,color:accepted?'#16a34a':'#dc2626'}}>{accepted?'Accepted':result.status==='not_available'?'Tests Unavailable':'Wrong Answer / Runtime Error'}</strong><div style={{fontSize:12,color:'#777',marginTop:5}}>{result.passed} / {result.total} test cases passed · {result.execution_time_ms} ms</div></div><strong style={{fontSize:14,color:'#555'}}>{result.score}%</strong></div>
   {tests.length>0&&<><div style={{display:'flex',gap:8,flexWrap:'wrap',marginBottom:15}}>{tests.map((t,i)=><button type="button" key={i} onClick={()=>setSelected(i)} style={{background:selected===i?'#ececec':'#f6f6f6',border:selected===i?'1px solid #a3a3a3':'1px solid transparent',borderRadius:7,padding:'8px 11px',fontSize:12,fontWeight:650,color:t.passed?'#15803d':'#dc2626',cursor:'pointer'}}>{t.passed?'✓':'✕'} {hidden(t,i)?`Hidden ${Math.max(1,i-publicTestCount+1)}`:`Case ${i+1}`}</button>)}</div>
   {chosen&&(privateCase?<div style={{...mono,background:'#fafafa'}}><strong>🔒 Hidden test case</strong>{'\n'}Result: {chosen.passed?'Passed':'Failed'}{'\n'}Inputs, expected values, and actual values are private.</div>:<><div style={{fontSize:13,fontWeight:700,color:'#555'}}>{chosen.name}</div>{(['input','expected','actual'] as const).map(field=><div key={field}><div style={muted}>{field==='input'?'Input':field==='expected'?'Expected Output':'Your Output'}</div><pre style={mono}>{field==='input'?(chosen.input??'Not provided by grader'):field==='expected'?(chosen.expected??chosen.expected_output??'Not provided by grader'):(chosen.actual??chosen.actual_output??'Not provided by grader')}</pre></div>)}{chosen.error&&<pre style={{...mono,color:'#dc2626'}}>{chosen.error}</pre>}</>)}
   </>}
   {result.error&&<pre style={{...mono,color:'#dc2626'}}>{result.error}</pre>}{result.stdout&&<><div style={muted}>Standard Output</div><pre style={mono}>{result.stdout}</pre></>}{result.stderr&&!submission&&<><div style={muted}>Error Output</div><pre style={mono}>{result.stderr}</pre></>}
   {!tests.length&&<div style={{fontSize:12,color:'#777'}}>This grader did not return individual test details.</div>}
   </>}
  </>}
  </div>
 </section>
}
