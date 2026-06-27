// function Header() {
//   return (
//     <header>
//       <h1>Legal Contract Analyzer</h1>

//       <p>
//         Upload a legal contract and ask questions using AI.
//       </p>

//       <hr />
//     </header>
//   );
// }

// export default Header;


function Header() {
  return (
    <header className="app-header">
      <div className="app-header__inner">

        <span className="app-header__eyebrow">⚖️ AI-Powered</span>

        <h1>Legal Contract Analyzer</h1>

        <p>
          Upload a legal contract and ask questions using AI.
        </p>

      </div>
    </header>
  );
}

export default Header;